from django.conf.urls import patterns, include, url
from django.contrib import admin

# Added for Django HTML5 Boilerplate
from dh5bp.urls import urlpatterns as dh5bp_urls

handler404 = 'dh5bp.views.page_not_found'
handler500 = 'dh5bp.views.server_error'

# URLs

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'LabNB.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
)

# some more dh5bp defaults (favicon.ico, apple-touch-icon.png, humans.txt, robots.txt, and crossdomain.xml)
urlpatterns += dh5bp_urls
