from django.conf.urls import patterns, url
from . import views


urlpatterns = patterns('',
    url(r'^$',views.view_all_objects),
    url(r'account/types/$',views.manage_acct_type),
    url(r'account/types/add',views.add_acct_type),
    url(r'account/types/edit/(?P<in_type_id>\d+)$',views.edit_acct_type),

    url(r'account/attributes/$',views.manage_acct_attribute),
    url(r'account/attributes/add',views.add_acct_attribute),
#    url(r'account/attribute/edit/(?P<in_type_id>\d+)$',views.edit_acct_type),

#    url(r'view_household',views.view_household),
#    url(r'user_management',views.view_persons),
#    url(r'address_management',views.view_addresses),
#    url(r'add_user',views.add_person),
#    url(r'edit_user/(?P<in_user_id>\d+)$',views.edit_person),
#    url(r'delete_user/(?P<in_user_id>\d+)$',views.delete_person),
#    url(r'^view_profile',views.view_profile),
#    url(r'^edit_profile',views.edit_profile),
)
