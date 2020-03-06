from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.db.models import Q
from hours.models import Hour
from checkout.models import Order


def make_search(request):
    """View that returns keyword searchs and renders search html with the results"""
    orders = Order.objects.filter(user=request.user,full_name__icontains=request.GET['Q'])
    orderByUser= Order.objects.filter(user=request.user)
    hours = Hour.objects.filter(Q(name__icontains=request.GET['Q'])|Q(comments__icontains=request.GET['Q']),order=orderByUser)
    orders = orders.order_by("date")
    hours = hours.order_by("order")
    total = hours.count()
    print(hours)
    return render(request,
                  "search.html",
                  {"orders": orders,
                  "hours": hours,
                  "total": total})
