from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from hours.models import Hour
from ProfessionalServices.models import PServices


def do_search(request):
    """View that returns keyword searchs and renders search html with the results"""
    print(request.GET['Q'])
    ProfessionalServices = PServices.objects.filter(
        name__icontains=request.GET['Q'])
    hours = Hour.objects.filter(
        name__icontains=request.GET['Q'])
    ProfessionalServices = ProfessionalServices.order_by("order")
    hours = hours.order_by("order")
    total = hours.count() + ProfessionalServices.count()
    return render(request,
                  "search.html",
                  {"ProfessionalServices": ProfessionalServices,
                  "hours": hours,
                  "total": total})
