from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.core.mail import send_mail
from django.contrib import auth, messages
from django.conf import settings
from django.contrib.auth.decorators import login_required
from .models import PServices, PServices_Bought
from .forms import RequestForm
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

users = []

def support_request_sent(request):
    """View to return after requesting an hour"""
    return render(request, 'request_support.html')
    
@login_required
def request_an_hour(request):
    """View handle support requests form"""
    if request.method == 'POST':
        request_form = RequestForm(request.POST)
        if request_form.is_valid():
            subject = request.POST['subject']
            date_required = request.POST['date_required']
            send_mail(
                subject,
                "Message from: " +
                request.POST['email'] +
                "Message: I would like to request an hour of support on " + date_required,
                'SERVER_EMAIL',
                ['debora199318@gmail.com'],
                fail_silently=False,
            )
            messages.success(request, "Your message has been sent!",
                                      extra_tags="alert-success")
            return redirect(reverse('support_request_sent'))
        else:
            messages.error(request, "Unable to send message at this time",
                                    extra_tags="alert-danger")
    else:
        request_form = RequestForm()
    return render(request, 'request_support.html', {'request_form': request_form})


def view_ProfessionalServices(request):
    """View to display all Professional Services"""
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
    or return 404 error if object is not found.
    """
    ProfService = get_object_or_404(PServices, pk=pk)
    if request.session.get('ProfService'):
        ProfServiceId = request.session.get('ProfService')

        if ProfServiceId != ProfService.pk:
            request.session['ProfService'] = ProfService.pk
            ProfService.save()
    else:
        request.session['ProfService'] = ProfService.pk
        ProfService.save()
    return render(request, "ProfService_detail.html")

