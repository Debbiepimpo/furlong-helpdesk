from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from hours.models import Hour
from ProfessionalServices.models import PServices


def do_search(request):
    """View that returns keyword searchs and renders search html with the results"""
    hours = Hour.objects.filter(
        name__icontains=request.GET['q']).exclude(
        status='Cancelled').exclude(
            status="Current Unavailable")
    ProfessionalServices = PServices.objects.filter(
        name__icontains=request.GET['q']).exclude(
        status='Cancelled').exclude(
            status="Current Unavailable")
    hours = hours.order_by("-purchases")
    ProfessionalServices = ProfessionalServices.order_by("-purchases")
    total = hours.count() + ProfessionalServices.count()
    return render(request,
                  "search.html",
                  {"hours": hours,
                   "ProfessionalServices": ProfessionalServices,
                   "total": total})
