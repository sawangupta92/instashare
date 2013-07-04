from django.conf.urls import patterns, include, url
from django.conf import settings
# import file_picker
# file_picker.autodiscover()
# Uncomment the next two lines to enable the admin:
# from django.contrib import admin
# admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'fileshare.views.home', name='home'),
    # url(r'^fileshare/', include('fileshare.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    # url(r'^admin/', include(admin.site.urls)),
    url(r'^view_of_create_company','sharing.views.view_of_create_company'),
    url(r'^view_of_delete_company','sharing.views.view_of_delete_company'),
    url(r'^create_company','sharing.views.create_company'),
    url(r'^delete_company','sharing.views.delete_company'),
    url(r'^create_employee','sharing.views.create_employee'),
    # url(r'^', include('filer.server.urls')),
    url(r'^view_of_create_employee','sharing.views.view_of_create_employee'),
    url(r'^view_of_delete_employee','sharing.views.view_of_delete_employee'),
    url(r'^delete_employee','sharing.views.delete_employee'),
    url(r'^view_of_login','sharing.views.view_of_login'),
    url(r'^mylogin','sharing.views.mylogin'), 
    url(r'^view_of_logout','sharing.views.view_of_logout'),
    url(r'^mylogout','sharing.views.mylogout'), 
    url(r'^view_of_update_company','sharing.views.view_of_update_company'),
    # url(r'^attachments/',include('attachments.urls')),
    url(r'^test','sharing.views.test'),
    url(r'^media/(?P<path>.*)$', 'django.views.static.serve', {'document_root': '/home/sawan/Desktop/instashare/fileshare/media/static/','show_indexes':True}),
    url(r'^view_of_upload_file','sharing.views.view_of_upload_file'),
    url(r'^upload_file','sharing.views.upload_file'),
    # url(r'^file-picker/',include(file_picker.site.urls)),
)