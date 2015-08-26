from django.conf.urls import patterns, url
from . import views


urlpatterns = patterns('',
    url(r'^$',views.user_home),
    url(r'profile',views.edit_profile),
    url(r'view_household',views.view_household),
    url(r'user_management',views.view_users),
    url(r'address_management',views.view_addresses),
    url(r'add_user',views.add_user),
#    url(r'^view_profile',views.view_profile),
#    url(r'^edit_profile',views.edit_profile),
)
