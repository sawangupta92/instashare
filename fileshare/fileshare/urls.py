from django.conf.urls import patterns, include, url

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
    url(r'^view_of_create_employee','sharing.views.view_of_create_employee'),
    url(r'^view_of_delete_employee','sharing.views.view_of_delete_employee'),
    url(r'^delete_employee','sharing.views.delete_employee'),
    url(r'^view_of_login','sharing.views.view_of_login'),
    url(r'^login','sharing.views.login'), 
    url(r'^view_of_logout','sharing.views.view_of_logout'),
    url(r'^logout','sharing.views.logout'), 
    url(r'^view_of_update_company','sharing.views.view_of_update_company'),
)
