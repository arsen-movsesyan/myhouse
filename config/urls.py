from django.conf.urls import patterns, url
from . import views


urlpatterns = patterns('',
    url(r'^$',views.view_all_objects),
    url(r'account/types/$',views.manage_acct_type),
    url(r'account/types/add$',views.add_acct_type),
    url(r'account/types/edit/(?P<in_type_id>\d+)$',views.edit_acct_type),

    url(r'account/attributes/$',views.manage_acct_attribute),
    url(r'account/attributes/add',views.add_acct_attribute),
    url(r'vehicle/types/$',views.manage_vehicle_type),
    url(r'vehicle/types/add',views.add_vehicle_type),

    url(r'document/types/$',views.manage_document_type),
    url(r'document/types/add$',views.add_document_type),
    url(r'document/types/edit/(?P<in_doc_type_id>\d+)$',views.edit_document_type),

    url(r'document/attributes/$',views.manage_doc_attribute),
    url(r'document/attributes/add$',views.add_doc_attribute),


#    url(r'document/types/attributes/add/(?P<in_doc_type_id>\d+)$',views.add_document_type_attribute),
#    url(r'document/types/add',views.add_document_type),

)
