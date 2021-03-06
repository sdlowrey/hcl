from django.conf.urls import patterns, include, url

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'hardview.views.home', name='home'),
    # url(r'^hardview/', include('hardview.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^hardware/', include('hardware.urls')),
    url(r'^certification/', include('certification.urls')),
)

handler500 = 'hardview.views.custom500'