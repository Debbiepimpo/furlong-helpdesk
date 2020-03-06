from django.conf.urls import url
from .views import make_search

urlpatterns = [
    url(r'^$', make_search, name='search')
]