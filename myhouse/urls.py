from django.conf.urls import include, url
#from django.contrib import admin

urlpatterns = [
    url(r'^$', 'account.views._index', name='home'),
    url(r'^register','account.views.self_register'),
    url(r'^login','account.views.log_in'),
    url(r'^logout','account.views.log_out'),
    url(r'^account/',include('account.urls')),
#    url(r'^admin/', include(admin.site.urls)),
]
