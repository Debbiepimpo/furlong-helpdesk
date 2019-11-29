from django.conf.urls import url, include
from .views import view_ProfessionalServices, ProfService_detail, add_or_edit_ProfService, delete_ProfService, view_completed_ProfessionalServices, delete_ProfService_comment, edit_ProfService_comments

urlpatterns = [
    url(r'^$', view_ProfessionalServices, name='view_ProfessionalServices'),
    url(r'^(?P<pk>\d+)/$', ProfService_detail, name='ProfService_detail'),
    url(r'^new/$', add_or_edit_ProfService, name='new_ProfService'),
    url(r'^(?P<pk>\d+)/edit/$', add_or_edit_ProfService, name="edit_ProfService"),
    url(r'^(?P<pk>\d+)/delete/$', delete_ProfService, name="delete_ProfService"),
    url(r'^completed_ProfessionalServices$', view_completed_ProfessionalServices, name='view_completed_ProfessionalServices'),
    url(r'^(?P<pk>\d+)/delete/comment$', delete_ProfService_comment, name="delete_ProfService_comment"),
    url(r'^(?P<pk>\d+)/edit_ProfService_comments/$', edit_ProfService_comments, name="edit_ProfService_comments"),
]
