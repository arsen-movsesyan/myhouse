from django.conf.urls import patterns, url
from . import views


urlpatterns = patterns('',
    url(r'^$',views.user_home),
    url(r'profile',views.edit_profile),
    url(r'view_household',views.view_household),
    url(r'user_management',views.view_persons),
    url(r'address_management',views.view_addresses),
    url(r'account_management/$',views.view_accounts),
    url(r'account_management/add_account$',views.add_account),
    url(r'account_management/edit_account/(?P<in_acct_id>\d)$',views.edit_account),
    url(r'add_user',views.add_person),
    url(r'edit_user/(?P<in_user_id>\d+)$',views.edit_person),
    url(r'delete_user/(?P<in_user_id>\d+)$',views.delete_person),
#    url(r'^view_profile',views.view_profile),
#    url(r'^edit_profile',views.edit_profile),
)
