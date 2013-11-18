from django.conf.urls import patterns, include, url

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'wigwamm_api.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^api/v1/repixl/', include('repixl.urls')),

    url(r'^admin/', include(admin.site.urls)),

    # hack this for now


)
