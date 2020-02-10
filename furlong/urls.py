"""furlong URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url, include
from django.contrib import admin
from accounts.views import index
from accounts import urls as accounts_urls
from hours import urls as urls_hours
from ProfessionalServices import urls as urls_ProfessionalServices
from cart import urls as urls_cart
from checkout import urls as urls_checkout
from search import urls as urls_search

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$', index, name="index"),
    url(r'^accounts/', include(accounts_urls)),
    url(r'^view_hours/', include(urls_hours)),
    url(r'^ProfessionalServices/', include(urls_ProfessionalServices)),
    url(r'^cart/', include(urls_cart)),
    url(r'^checkout/', include(urls_checkout)),
    url(r'^search/', include(urls_search))

]
