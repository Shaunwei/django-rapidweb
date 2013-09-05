from django.conf.urls import patterns, include, url
from payments import views
import settings

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
    url(r'^sign_in$', views.sign_in, name='sign_in'),
    url(r'^sign_out$', views.sign_out, name='sign_out'),
    url(r'^register$', views.register, name='register'),
    url(r'^edit$', views.edit, name='edit'),
    (r'^media/(?P<path>.*)$', 'django.views.static.serve',
                 {'document_root': settings.MEDIA_ROOT}),
)
