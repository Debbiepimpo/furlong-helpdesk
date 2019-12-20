from django.conf.urls import url, include
from .views import view_ProfessionalServices, ProfService_detail, request_an_hour, view_completed_ProfessionalServices

urlpatterns = [
    url(r'^$', view_ProfessionalServices, name='view_ProfessionalServices'),
    url(r'^(?P<pk>\d+)/$', ProfService_detail, name='ProfService_detail'),
    url(r'^requestSupport/$', request_an_hour, name='request_support'),
    url(r'^completed_ProfessionalServices$', view_completed_ProfessionalServices, name='view_completed_ProfessionalServices'),
    
]
