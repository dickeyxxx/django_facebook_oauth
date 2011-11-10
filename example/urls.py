from django.conf.urls.defaults import patterns, include, url

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    url(r'^$', 'example.views.home'),

    url(r'^facebook/login$', 'facebook.views.login'),
    url(r'^facebook/authentication_callback$',
                                    'facebook.views.authentication_callback'),
    url(r'^logout$', 'django.contrib.auth.views.logout'),

    url(r'^admin/', include(admin.site.urls)),
)
