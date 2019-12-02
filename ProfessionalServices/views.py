from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .models import PServices, PServices_Bought
from .forms import CreatePServicesForm, PServicesCommentForm
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

users = []


def view_ProfessionalServices(request):
    """View to display all Professional Services excluding those with cancelled or done status"""
    ProfessionalServices = PServices.objects.all().order_by(
        '-id').exclude(status='Cancelled').exclude(status="Current Unavailable")
    paginator = Paginator(ProfessionalServices, 5)  # Show 5 ProfessionalServices per page

    page = request.GET.get('page')
    try:
        ProfessionalServices = paginator.page(page)
    except PageNotAnInteger:
        ProfessionalServices = paginator.page(1)
    except EmptyPage:
        ProfessionalServices = paginator.page(paginator.num_pages)
    return render(request, "ProfessionalServices.html", {"ProfessionalServices": ProfessionalServices})


def view_completed_ProfessionalServices(request):
    """View to display completed ProfessionalServices"""
    ProfessionalServices = PServices.objects.all().order_by('-id').filter(status='Current Unavailable')
    paginator = Paginator(ProfessionalServices, 5)  # Show 5 ProfessionalServices per page

    page = request.GET.get('page')
    try:
        ProfessionalServices = paginator.page(page)
    except PageNotAnInteger:
        ProfessionalServices = paginator.page(1)
    except EmptyPage:
        ProfessionalServices = paginator.page(paginator.num_pages)
    return render(request, "completed_ProfessionalServices.html", {"ProfessionalServices": ProfessionalServices})


def ProfService_detail(request, pk):
    """
    Create a view that returns a single
    ProfService object based on the ProfService ID (pk) and
    render it to the ProfService_detail.html template
    or return 404 error if object is not found
    Also handles commenting on the ProfService as well
    as regulating the amount of views attributed
    to the ProfService.
    """
    ProfService = get_object_or_404(PServices, pk=pk)
    if request.method == "POST":

        form = PServicesCommentForm(request.POST)

        if form.is_valid():
            ProfServiceComment = form.save(commit=False)
            ProfServiceComment.ProfService = ProfService
            ProfServiceComment.author = request.user
            ProfService.comment_number += 1
            ProfService.save()
            ProfServiceComment.save()
            return redirect(reverse('ProfService_detail', kwargs={'pk': pk}))
        else:
            messages.error(
                request,
                "Looks like your comment is empty!",
                extra_tags="alert-danger")
            form = PServicesCommentForm(instance=ProfService)
            return redirect(reverse('ProfService_detail', kwargs={'pk': pk}))

    else:
        form = PServicesCommentForm()
        comments = PServices_Bought.objects.filter(ProfService__pk=ProfService.pk)
        comments_total = len(comments)
        response = render(request,
                          'ProfService_detail.html',
                          {'ProfService': ProfService,
                           'comments': comments,
                           'comments_total': comments_total,
                           'form': form})
        if request.session.get('ProfService'):
            ProfServiceId = request.session.get('ProfService')

            if ProfServiceId != ProfService.pk:
                request.session['ProfService'] = ProfService.pk
                ProfService.views += 1
                ProfService.save()
        else:
            request.session['ProfService'] = ProfService.pk
            ProfService.views += 1
            ProfService.save()
        return response


@login_required
def add_or_edit_ProfService(request, pk=None):
    """View to add or edit ProfService, if you are the ProfService creator"""
    ProfService = get_object_or_404(PServices, pk=pk) if pk else None
    if ProfService is not None:
        author = ProfService.author
        if author == request.user:
            if request.method == "POST":
                form = CreatePServicesForm(request.POST, instance=ProfService)

                if form.is_valid():
                    ProfService = form.save(commit=False)
                    ProfService.author = request.user
                    ProfService.save()
                    return redirect(ProfService_detail, ProfService.pk)
            else:
                form = CreatePServicesForm(instance=ProfService)
            return render(request, 'create_ProfService.html', {'form': form})
        else:
            messages.error(
                request,
                "This is not yours to edit!",
                extra_tags="alert-danger")
            return redirect(reverse('index'))
    else:
        if request.method == "POST":
            form = CreatePServicesForm(request.POST)
            if form.is_valid():
                ProfService = form.save(commit=False)
                ProfService.author = request.user
                ProfService.save()
                return redirect(reverse('view_ProfessionalServices'))
        else:
            form = CreatePServicesForm()
        return render(request, 'create_ProfService.html', {'form': form})


@login_required()
def delete_ProfService(request, pk):
    """View to delete ProfService if user created it"""
    ProfService = get_object_or_404(PServices, pk=pk)
    author = ProfService.author
    if author == request.user:
        ProfService.delete()
    else:
        messages.error(
            request,
            "This is not yours to delete!",
            extra_tags="alert-danger")
        return redirect(reverse('index'))
    return redirect('profile')


@login_required
def delete_ProfService_comment(request, pk):
    comment = get_object_or_404(PServices_Bought, pk=pk)
    ProfService = comment.ProfService
    if request.user == comment.author:
        comment.ProfService.comment_number -= 1
        ProfService.save()
        comment.delete()
        messages.success(request, 'This comment has been deleted.',
                         extra_tags="alert-success")
    else:
        messages.info(request,
                      'You do not have permission to delete this comment.')
    return redirect('ProfService_detail', pk=ProfService.pk)


@login_required()
def edit_ProfService_comments(request, pk):
    """
    This view allows the author of a comment to
    edit it. Other users who try to
    access this function using the url will be
    redirected to a blank form where they can
    add a new comment.
    """
    comment = get_object_or_404(PServices_Bought, pk=pk)
    ProfService = comment.ProfService
    if request.user == comment.author:
        if request.method == "POST":
            form = PServicesCommentForm(request.POST, instance=comment)
            if form.is_valid():
                form.save()
                return redirect('ProfService_detail', pk=ProfService.pk)
        else:
            form = PServicesCommentForm(instance=comment)
        return render(request, "edit_ProfService_comments.html", {"form": form})
    else:
        messages.info(request,
                      'You do not have permission to edit this comment.')
        form = PServicesCommentForm()
    return redirect('ProfService_detail', pk=ProfService.pk)