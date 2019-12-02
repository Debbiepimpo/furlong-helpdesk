from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from datetime import datetime
from django.contrib import messages
from .models import Hour, HourComment, HourUpvote
from .forms import CreateHourForm, HourCommentForm
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger


def view_hours(request):
    """View that displays all hours excluding cancelled or done status"""
    hours = Hour.objects.all().order_by(
        '-id').exclude(status='Cancelled').exclude(status="Current Unavailable")
    paginator = Paginator(hours, 5)  # Show 5 hours per page

    page = request.GET.get('page')
    try:
        hours = paginator.page(page)
    except PageNotAnInteger:
        hours = paginator.page(1)
    except EmptyPage:
        hours = paginator.page(paginator.num_pages)

    return render(request, "hours.html", {"hours": hours})


def view_completed_hours(request):
    """View that displays completed hours"""
    hours = Hour.objects.all().order_by('-id').filter(status='Current Unavailable')

    paginator = Paginator(hours, 5)  # Show 5 hours per page

    page = request.GET.get('page')
    try:
        hours = paginator.page(page)
    except PageNotAnInteger:
        hours = paginator.page(1)
    except EmptyPage:
        hours = paginator.page(paginator.num_pages)
    return render(request, "completed_hours.html", {"hours": hours})


def hour_detail(request, pk):
    """
    Create a view that returns a single
    hour object based on the hour ID (pk) and
    render it to the hour_detail.html template
    or return 404 error if object is not found
    Also handles commenting on the hour as well
    as regulating the amount of views attributed
    to the hour.
    """
    hour = get_object_or_404(Hour, pk=pk)
    if request.method == "POST":

        form = HourCommentForm(request.POST)

        if form.is_valid():
            hourComment = form.save(commit=False)
            hourComment.hour = hour
            hourComment.author = request.user
            hour.comment_number += 1
            hour.save()
            hourComment.save()
            return redirect(reverse('hour_detail', kwargs={'pk': pk}))
        else:
            messages.error(
                request,
                "Looks like your comment is empty!",
                extra_tags="alert-danger")
            form = HourCommentForm(instance=hour)
            return redirect(reverse('hour_detail', kwargs={'pk': pk}))

    else:
        form = HourCommentForm()
        comments = HourComment.objects.filter(hour__pk=hour.pk)
        comments_total = len(comments)
        response = render(request,
                          'hour_detail.html',
                          {'hour': hour,
                           'comments': comments,
                           'comments_total': comments_total,
                           'form': form})
        if request.session.get('hour'):
            hourId = request.session.get('hour')

            if hourId != hour.pk:
                request.session['hour'] = hour.pk
                hour.views += 1
                hour.save()
        else:
            request.session['hour'] = hour.pk
            hour.views += 1
            hour.save()
        return response


@login_required()
def upvote_hour(request, pk):
    """
    Stops user voting multiple times if they have already.
    """
    hour = Hour.objects.get(pk=pk)
    if HourUpvote.objects.filter(user=request.user, hour=hour):
        messages.error(
            request,
            "You have upvoted this hour already!",
            extra_tags="alert-danger")
    else:
        hour.upvotes += 1
        hour.save()
        HourUpvote.objects.create(user=request.user, hour=hour)
        messages.success(
            request,
            "Your vote has been accepted!",
            extra_tags="alert-success")
    return redirect('view_hours')


@login_required
def add_or_edit_hour(request, pk=None):
    """View to edit or add a hour. Checks if user editing is the creator"""
    hour = get_object_or_404(Hour, pk=pk) if pk else None
    if hour is not None:
        author = hour.author
        if author == request.user:
            if request.method == "POST":
                form = CreateHourForm(request.POST, instance=hour)
                if form.is_valid():
                    hour = form.save(commit=False)
                    hour.author = request.user
                    hour.save()
                    return redirect(hour_detail, hour.pk)
            else:
                form = CreateHourForm(instance=hour)
            return render(request, 'create_hour.html', {'form': form})
        else:
            messages.error(
                request,
                "This is not yours to edit!",
                extra_tags="alert-danger")
            return redirect(reverse('index'))
    else:
        if request.method == "POST":
            form = CreateHourForm(request.POST)
            if form.is_valid():
                hour = form.save(commit=False)
                hour.author = request.user
                hour.save()
                return redirect(reverse('view_hours'))
        else:
            form = CreateHourForm()
        return render(request, 'create_hour.html', {'form': form})


@login_required
def delete_hour(request, pk):
    """View to delete a hour if user created selected hour"""
    hour = get_object_or_404(Hour, pk=pk)
    author = hour.author
    if author == request.user:
        hour.delete()
    else:
        messages.error(
            request,
            "This is not yours to delete!",
            extra_tags="alert-danger")
        return redirect(reverse('index'))
    return redirect('profile')


@login_required
def delete_hour_comment(request, pk):
    comment = get_object_or_404(HourComment, pk=pk)
    hour = comment.hour
    if request.user == comment.author:
        comment.hour.comment_number -= 1
        hour.save()
        comment.delete()
        messages.success(request, 'This comment has been deleted.',
                         extra_tags="alert-success")
    else:
        messages.info(request,
                      'You do not have permission to delete this comment.')
    return redirect('hour_detail', pk=hour.pk)


@login_required()
def edit_hour_comments(request, pk):
    """
    This view allows the author of a comment to
    edit it. Other users who try to
    access this function using the url will be
    redirected to a blank form where they can
    add a new comment.
    """
    comment = get_object_or_404(HourComment, pk=pk)
    hour = comment.hour
    if request.user == comment.author:
        if request.method == "POST":
            form = HourCommentForm(request.POST, instance=comment)
            if form.is_valid():
                form.save()
                return redirect('hour_detail', pk=hour.pk)
        else:
            form = HourCommentForm(instance=comment)
        return render(request, "edit_hour_comments.html", {"form": form})
    else:
        messages.info(request,
                      'You do not have permission to edit this comment.')
        form = HourCommentForm()
    return redirect('hour_detail', pk=hour.pk)
