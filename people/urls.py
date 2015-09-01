from django.conf.urls import patterns, url
from . import views


urlpatterns = patterns('',
    url(r'^$',views.view_persons),
    url(r'add',views.add_person),
    url(r'edit/(?P<in_user_id>\d+)$',views.edit_person),
    url(r'delete/(?P<in_user_id>\d+)$',views.delete_person),
    url(r'profile$',views.edit_profile),
)
