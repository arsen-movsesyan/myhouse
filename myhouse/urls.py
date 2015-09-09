from django.conf.urls import include, url
from . import views

from django.contrib import admin

urlpatterns = [
    url(r'^$', views._index),
    url(r'^register',views.self_register),
    url(r'^login',views.log_in),
    url(r'^logout',views.log_out),
    url(r'^account/',include('account.urls')),
    url(r'^people/',include('people.urls')),
    url(r'^config/',include('config.urls')),
    url(r'^vehicle/',include('vehicle.urls')),
    url(r'^admin/', include(admin.site.urls)),
]
