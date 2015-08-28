from django.conf.urls import patterns, url
from . import views


urlpatterns = patterns('',
    url(r'^$',views.view_all_objects),
    url(r'acct_type/$',views.manage_acct_type),
    url(r'acct_type/add_acct_type',views.add_acct_type),
    url(r'acct_type/edit_acct_type/(?P<in_type_id>\d+)$',views.edit_acct_type),
#    url(r'view_household',views.view_household),
#    url(r'user_management',views.view_persons),
#    url(r'address_management',views.view_addresses),
#    url(r'add_user',views.add_person),
#    url(r'edit_user/(?P<in_user_id>\d+)$',views.edit_person),
#    url(r'delete_user/(?P<in_user_id>\d+)$',views.delete_person),
#    url(r'^view_profile',views.view_profile),
#    url(r'^edit_profile',views.edit_profile),
)
