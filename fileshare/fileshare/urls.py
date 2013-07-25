from django.conf.urls import patterns, include, url
from django.conf import settings
from django.views.generic import TemplateView
# from sharing.views import archive
# import django.views.generic.date_based as views
from django.views.generic import dates as view
from django.contrib.auth.decorators import login_required
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
######################## URL OF COMPANY ###############################
    url(r'^view_of_create_company','sharing.views.view_of_create_company'),
    url(r'^view_of_delete_company','sharing.views.view_of_delete_company'),
    url(r'^create_company','sharing.views.create_company'),
    url(r'^delete_company','sharing.views.delete_company'),
    url(r'^view_of_update_company','sharing.views.view_of_update_company'),
    url(r'^company_save_update','sharing.views.company_save_update'),
    url(r'^company','sharing.views.company_operations'),
    # url(r'^', include('filer.server.urls')),

######################## URL OF EMPLOYEE ###############################
    url(r'^create_employee','sharing.views.create_employee'),
    url(r'^view_of_delete_employee','sharing.views.view_of_delete_employee'),
    url(r'^delete_employee','sharing.views.delete_employee'),
    url(r'^view_of_create_employee','sharing.views.view_of_create_employee'),
    url(r'^view_of_update_employee/(?P<name>.*)$','sharing.views.view_of_update_employee'),
    url(r'^employee_save_update','sharing.views.employee_save_update'),
    # url(r'^attachments/',include('attachments.urls')),

######################## URL OF INDEX ###############################
    url(r'^mylogout','sharing.views.mylogout'), 
    url(r'^mylogin','sharing.views.mylogin'), 
    url(r'^view_of_logout','sharing.views.view_of_logout'),
    url(r'^view_of_login','sharing.views.view_of_login'),
    url(r'^test','sharing.views.test'),
    url(r'^newt','sharing.views.newt'),
    url(r'^save_newt','sharing.views.save_newt'),
    url(r'^index','sharing.views.index'),
    url(r'^fail','sharing.views.fail'),
    url(r'^sign_up','sharing.views.sign_up', name='sign_up'),
    url(r'^view_of_sign_up','sharing.views.view_of_sign_up'),
    url(r'^home_page','sharing.views.home_page'),
    url(r'^employee_already_associated_with_company_fail','sharing.views.employee_already_associated_with_company_fail'),
    # (r'^tinymce/', include('tinymce.urls')),
    # (r'^search/', include('haystack.urls')),
    url(r'^search_result','sharing.views.search_result'),


######################## URL OF FILE ###############################
    url(r'^media/(?P<path>.*)$','django.views.static.serve', {'document_root': settings.MEDIA_ROOT,'show_indexes':True}),
    url(r'^view_of_upload_file','sharing.views.view_of_upload_file'),
    url(r'^upload_file','sharing.views.upload_file'),
    url(r'^view_of_my_file','sharing.views.view_of_my_file'),
    url(r'^view_my_company_file','sharing.views.view_my_company_file'),
    url(r'^delete_my_file','sharing.views.delete_my_file'),
    url(r'^view_of_delete_file','sharing.views.view_of_delete_file'),
    url(r'^show_file','sharing.views.show_file'),
    url(r'^social/', include('socialregistration.urls', namespace = 'socialregistration')),
    # url(r'^fileshare'),
    # url(r'^media/')

    # url(r'^file-picker/',include(file_picker.site.urls)),
    # http://stackoverflow.com/questions/1539697/can-i-filter-on-request-user-when-using-django-generic-views
)