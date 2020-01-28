from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from datetime import datetime
from django.contrib import messages
from .models import Hour
from checkout.models import Order
from ProfessionalServices.models import PServices
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger


def view_hours(request):
    """View that displays all hours excluding cancelled or done status"""
    orders = Order.objects.filter(user_id=request.user.id).order_by('-id').exclude(status='Inactive')
    totalHours=0
    totalHoursRequested=0
    ProfessionalServices = []
    hours = []
    for order in orders:
        totalHours+=order.remainingHours
        ProfessionalServices.append(get_object_or_404(PServices, pk=order.ProfService_id))
        requestedHours = Hour.objects.filter(order_id=order).order_by('id')
        for requestedHour in requestedHours:
            totalHoursRequested+=requestedHour.requested_hours
            hours.append(requestedHour)
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
