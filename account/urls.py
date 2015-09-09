from django.conf.urls import patterns, url
from account import views


urlpatterns = patterns('',
    url(r'^$',views.view_accounts,{'view_filter':'active'}),
    url(r'^view_all$',views.view_accounts,{'view_filter':'all'}),
    url(r'^view_time_watch$',views.view_time_watch),
#    url(r'^view_time_watch$',views.view_accounts,{'view_filter':'time_watch'}),

    url(r'add$',views.add_account),
    url(r'view/(?P<in_acct_id>\d+)$',views.view_account),
    url(r'edit/(?P<in_acct_id>\d+)$',views.edit_account),
    url(r'delete/(?P<in_acct_id>\d+)$',views.delete_account),
    url(r'time_watch/(?P<in_acct_id>\d+)$',views.make_time_watch),
    url(r'acknowledge/(?P<in_acct_id>\d+)$',views.acknowledge),
    url(r'history/(?P<in_acct_id>\d+)$',views.view_payment_history),
)
