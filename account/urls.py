from django.conf.urls import patterns, url
from . import views


urlpatterns = patterns('',
    url(r'^$',views.user_home),
    url(r'edit_user',views.edit_user),
    url(r'view_household',views.view_household),
#    url(r'^view_profile',views.view_profile),
#    url(r'^edit_profile',views.edit_profile),
)
