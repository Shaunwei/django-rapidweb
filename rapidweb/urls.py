from django.conf.urls import patterns, include, url

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'rapidweb.views.home', name='home'),
    # url(r'^rapidweb/', include('rapidweb.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),
    url(r'^$', 'main.views.index',name='home'),
    ('^pages/', include('django.contrib.flatpages.urls')),
    url(r'^contact/','contact.views.contact',name='contact'),
)
