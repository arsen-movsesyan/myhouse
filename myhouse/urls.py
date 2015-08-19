from django.conf.urls import include, url
#from django.contrib import admin

urlpatterns = [
    url(r'^$', 'myhouse.views.home', name='home'),
    url(r'^register','myhouse.views.register'),
    url(r'^login','myhouse.views.log_in'),
    url(r'^logout','myhouse.views.log_out'),
    url(r'^account/',include('account.urls')),
#    url(r'^admin/', include(admin.site.urls)),
]
