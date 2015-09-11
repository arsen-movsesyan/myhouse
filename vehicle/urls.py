from django.conf.urls import patterns, url
from vehicle import views


urlpatterns = patterns('',
    url(r'^$',views.view_vehicles),
    url(r'view_all$',views.view_vehicles),
    url(r'view_time_watch$',views.view_time_watch),
    url(r'add$',views.add_vehicle_car),
    url(r'view/(?P<in_vehicle_id>\d+)$',views.view_vehicle),
    url(r'renewal_acknowledge/(?P<in_vehicle_id>\d+)$',views.renewal_acknowledge),
    url(r'edit/(?P<in_vehicle_id>\d+)$',views.edit_vehicle_car),
#    url(r'delete/(?P<in_acct_id>\d+)$',views.delete_account),
)
