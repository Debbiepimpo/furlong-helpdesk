from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.core.mail import send_mail
from django.contrib import auth, messages
from django.conf import settings
from django.contrib.auth.decorators import login_required
from .models import PServices
from .forms import RequestForm
from hours.forms import HourForm
from checkout.models import Order
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

users = []

    
@login_required
def request_an_hour(request):
    """View handle support requests form"""
    if request.method == 'POST':
        request_form = RequestForm(request.user,request.POST)
        if request_form.is_valid():
            name = request.POST['name']
            subject = request.POST['subject']
            date_required = request.POST['date_required']
            start_time = request.POST['start_time']
            finish_time = request.POST['finish_time']
            order_id = request.POST['package']
            order_data = get_object_or_404(Order, pk=order_id)
            hourForm = HourForm()
            requestedHour = hourForm.save(commit=False)
            requestedHour.name = name
            sh, sm = start_time.split(':')
            fh, fm = finish_time.split(':')
            requested_hours = int(fh)-int(sh)
            requestedHour.requested_hours = requested_hours
            requestedHour.requested_date = date_required
            requestedHour.order = order_data
            requestedHour.save()
            order_data.remainingHours = (order_data.remainingHours - requested_hours)
            order_data.save()
            send_mail(
                subject,
                "Message from: " +
                request.POST['email'] + 
                "\nMessage: I would like to request support on " + date_required + " from "+ start_time + " to " + finish_time,
                'SERVER_EMAIL',
                ['deboraperaltaorozco@gmail.com'],
                fail_silently=False,
            )
            messages.success(request, "Your message has been sent!",
                                      extra_tags="alert-success")
            return redirect(reverse('index'))
        else:
            messages.error(request, "Unable to send message at this time",
                                    extra_tags="alert-danger")
    else:
        request_form = RequestForm(request.user)
    return render(request, 'request_support.html', {'request_form': request_form})


def view_ProfessionalServices(request):
    """View to display all Professional Services"""
    ProfessionalServices = PServices.objects.all().order_by(
        '-id').exclude(status="Current Unavailable")
    paginator = Paginator(ProfessionalServices, 5)  # Show 5 Professional Services per page

    page = request.GET.get('page')
    try:
        ProfessionalServices = paginator.page(page)
    except PageNotAnInteger:
        ProfessionalServices = paginator.page(1)
    except EmptyPage:
        ProfessionalServices = paginator.page(paginator.num_pages)
    return render(request, "ProfessionalServices.html", {"ProfessionalServices": ProfessionalServices})


def ProfService_detail(request, pk):
    """
    This view that returns a single
    ProfService object details or if is not found
    return 404 error if object is not found.
    """
    ProfService = get_object_or_404(PServices, pk=pk)
    
    return render(request, "ProfService_detail.html",  {"ProfService": ProfService})

