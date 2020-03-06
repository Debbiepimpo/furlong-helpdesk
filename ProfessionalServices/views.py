from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.core.mail import send_mail
from django.contrib import auth, messages
from django.conf import settings
from django.contrib.auth.decorators import login_required
from accounts.forms import UserLoginForm, UserRegistrationForm, ContactForm
from datetime import timedelta
from .models import PServices
from .forms import RequestForm
from hours.forms import HourForm
from checkout.models import Order
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

users = []

    
@login_required
def request_an_hour(request):
    """This piece of code allows to send an email to the admin
    about requesting training hours with the time, date, amount 
    of hours and from which package if the user bought same package
    more than once"""
    
    if request.method == 'POST':
        request_form = RequestForm(request.user,request.POST)
        if request_form.is_valid():
            request.user.first_name
            request.user.last_name
            subject = request.POST['subject']
            date_required = request.POST['date_required']
            start_time = request.POST['start_time']
            hours = request.POST['hours']
            order_id = request.POST['package']
            order_data = get_object_or_404(Order, pk=order_id)
            try:
                send_mail(
                    subject,
                    "Message from: " +
                    request.user.email + 
                    "\nMessage: I would like to request support on " + date_required + " from "+ start_time + " for " + hours + " hours ",
                    'SERVER_EMAIL',
                    ['deboraperaltaorozco@gmail.com'],
                    fail_silently=False,
                )
                
                """This piece of code below allows to save the 
                requested hours on database and make the deductions 
                from available hours"""
                
                hourForm = HourForm()
                requestedHour = hourForm.save(commit=False)
                requestedHour.name = request.user.first_name + request.user.last_name
                requestedHour.requested_hours = hours
                requestedHour.requested_date = date_required + " " + start_time
                requestedHour.order = order_data
                requestedHour.save()
                order_data.remainingHours = (order_data.remainingHours - int(hours))
                order_data.save()
                messages.success(request, "Your message has been sent!",
                                          extra_tags="alert-success")
                return redirect(reverse('view_hours'))
            except Exception as err:
                messages.error(request, "Oops! Something went wrong.",
                                          extra_tags="alert-success")
                print("error: {0}".format(err))
                return redirect(reverse('profile'))
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

