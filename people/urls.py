from django.conf.urls import patterns, url
from . import views


urlpatterns = patterns('',
    url(r'^$',views.view_persons),
    url(r'add',views.add_person),
    url(r'view/(?P<in_user_id>\d+)$',views.view_person),
    url(r'documents/(?P<in_user_id>\d+)/$',views.manage_documents),
    url(r'documents/(?P<in_user_id>\d+)/assign_doc/(?P<in_doc_id>\d+)/$',views.assign_document),
    url(r'edit/(?P<in_user_id>\d+)$',views.edit_person),
    url(r'delete/(?P<in_user_id>\d+)$',views.delete_person),
    url(r'profile$',views.edit_profile),
)
