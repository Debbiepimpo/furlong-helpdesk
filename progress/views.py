from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from .progress import HourBarChart, PServicesBarChart, HourPieChart, PServicesPieChart


def progress(request):
    """A view that displays the progress page"""
    return render(request,
                  "progress.html",
                  {'hour_bar_chart': HourBarChart,
                   'ProfService_bar_chart': PServicesBarChart,
                   'hour_pie_chart': HourPieChart,
                   'ProfService_pie_chart': PServicesPieChart})
