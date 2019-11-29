import pygal
from hours.models import Hour
from ProfessionalServices.models import PServices
from pygal.style import Style

"""Custom styles for progress"""
custom_style = Style(
    background='transparent',
    plot_background='transparent',
    font_family='Roboto',
    legend_font_size=25,
    value_font_size=25,
    label_font_size=25,
    major_label_font_size=25,
    colors=('#072F5F', '#1261A0', '#2780E3', '#3895D3', '#58CCED'))


def hour_bar_chart():
    """A bar chart showing the 5 most upvoted hours in descending order"""

    hours = Hour.objects.order_by('-upvotes')[:5]
    bar_chart = pygal.Bar(
        show_minor_y_labels=False,
        print_values=True,
        print_zeroes=False,
        style=custom_style
    )

    for hour in hours:
        bar_chart.add(hour.name, hour.upvotes)

    return bar_chart.render()


def HourBarChart():
    """Enable importing the graph into a view"""

    chart = hour_bar_chart()
    return chart


def ProfService_bar_chart():
    """A bar chart showing the 5 most upvoted Professional Services in descending order"""

    ProfessionalServices = PServices.objects.order_by('-upvotes')[:5]
    bar_chart = pygal.Bar(
        show_minor_y_labels=False,
        print_values=True,
        print_zeroes=False,
        style=custom_style
    )

    for ProfService in ProfessionalServices:
        bar_chart.add(ProfService.name, ProfService.upvotes)

    return bar_chart.render()


def PServicesBarChart():
    """Enable importing the graph into a view"""

    chart = ProfService_bar_chart()
    return chart


def hour_pie_chart():
    """A pie chart showing the status of hours"""

    todo = Hour.objects.filter(status='To do').count()
    inprogress = Hour.objects.filter(status='In progress').count()
    done = Hour.objects.filter(status='Done').count()
    cancelled = Hour.objects.filter(status='Cancelled').count()
    p_chart = pygal.Pie(
        print_values=True,
        style=custom_style,
    )

    p_chart.add('To Do', todo)
    p_chart.add('In Progress', inprogress)
    p_chart.add('Done', done)
    p_chart.add('Cancelled', cancelled)
    return p_chart.render()


def HourPieChart():
    """Enable importing the graph into a view"""

    chart = hour_pie_chart()
    return chart


def ProfService_pie_chart():
    """A pie chart showing the status of Professional Services"""

    todo = PServices.objects.filter(status='To do').count()
    inprogress = PServices.objects.filter(status='In progress').count()
    done = PServices.objects.filter(status='Done').count()
    cancelled = PServices.objects.filter(status='Cancelled').count()
    p_chart = pygal.Pie(
        print_values=True,
        style=custom_style
    )

    p_chart.add('To Do', todo)
    p_chart.add('In Progress', inprogress)
    p_chart.add('Done', done)
    p_chart.add('Cancelled', cancelled)
    return p_chart.render()


def PServicesPieChart():
    """Enable importing the graph into a view"""

    chart = ProfService_pie_chart()
    return chart
