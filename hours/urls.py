from django.conf.urls import url, include
from .views import view_hours, hour_detail, upvote_hour, add_or_edit_hour, delete_hour, view_completed_hours, delete_hour_comment, edit_hour_comments

urlpatterns = [
    url(r'^$', view_hours, name='view_hours'),
    url(r'^(?P<pk>\d+)/$', hour_detail, name='hour_detail'),
    url(r'^upvote(?P<pk>\d+)/$', upvote_hour, name='upvote_hour'),
    url(r'^new/$', add_or_edit_hour, name='new_hour'),
    url(r'^(?P<pk>\d+)/edit/$', add_or_edit_hour, name="edit_hour"),
    url(r'^(?P<pk>\d+)/delete/$', delete_hour, name="delete_hour"),
    url(r'^complete_hours$', view_completed_hours, name='view_completed_hours'),
    url(r'^(?P<pk>\d+)/delete/comment$', delete_hour_comment, name="delete_hour_comment"),
    url(r'^(?P<pk>\d+)/edit_hour_comments/$', edit_hour_comments, name="edit_hour_comments"),
]
