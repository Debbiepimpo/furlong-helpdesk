from django.conf.urls import url
from .views import progress

urlpatterns = [
    url(r'^$', progress, name="progress"),
]