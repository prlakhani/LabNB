from django.conf.urls import patterns, include, url
from django.contrib import admin

# Added for Django HTML5 Boilerplate
from dh5bp.urls import urlpatterns as dh5bp_urls

handler404 = 'dh5bp.views.page_not_found'
handler500 = 'dh5bp.views.server_error'

# Added for simple templates like homepage
from django.views.generic import TemplateView

# URLs

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'LabNB.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    
    # http://stackoverflow.com/questions/1940528/django-index-page-best-most-common-practice
    url(r'^$', TemplateView.as_view(template_name="LabNB/index.html")),
    url(r'^accounts/login/$', 'django.contrib.auth.views.login'),
    url(r'^admin/', include(admin.site.urls)),
)

# some more dh5bp defaults (favicon.ico, apple-touch-icon.png, humans.txt, robots.txt, and crossdomain.xml)
urlpatterns += dh5bp_urls
