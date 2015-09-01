from django.conf.urls import patterns, url
from . import views


urlpatterns = patterns('',
    url(r'^$',views.view_accounts,{'view_filter':'active'}),
    url(r'^view_all$',views.view_accounts,{'view_filter':'all'}),
    url(r'^view_time_watch$',views.view_time_watch),

    url(r'add$',views.add_account),
    url(r'view/(?P<in_acct_id>\d)$',views.view_account),
    url(r'edit/(?P<in_acct_id>\d)$',views.edit_account),
)
