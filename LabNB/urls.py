from django.conf.urls import patterns, include, url
from django.contrib import admin
from django.conf import settings
from LabNB import views     # This lets us use the custom error handlers, as well as an index view with context, if desired.

# These handlers override the default error page provided by Django.
# Django looks for these var names specifically in the urlconf.

handler404 = 'LabNB.views.page_not_found'
handler500 = 'LabNB.views.server_error'

# Added for simple templates like homepage, or icons
from django.views.generic import TemplateView, RedirectView

# URLs
urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'LabNB.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    # http://stackoverflow.com/questions/1940528/django-index-page-best-most-common-practice

    # OMG CRAZY NOTE: namespace ABSOLUTELY MUST BE IN DOUBLEQUOTES to work.
    
    url(r'^$', views.index, name='index'),
    url(r'accounts/login/', 'django.contrib.auth.views.login'),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^labinv/', include('labinv.urls', namespace="labinv")),
    url(r'^data/', include('data.urls', namespace="data")),
    url(r'^apple-touch-icon\.png$', RedirectView.as_view(
        url='%simg/apple-touch-icon.png' % settings.STATIC_URL)),
    url(r'^crossdomain\.xml$', TemplateView.as_view(
	   template_name='crossdomain.xml')),
    url(r'^favicon\.ico$', RedirectView.as_view(
	   url='%simg/favicon.ico' % settings.STATIC_URL)),
    url(r'^humans\.txt', TemplateView.as_view(
	   template_name='humans.txt')),
	url(r'^robots\.txt', TemplateView.as_view(
		template_name='robots.txt')),
)

urlpatterns += patterns('', (
        r'^static/(?P<path>.*)$',
        'django.views.static.serve',
        {'document_root': settings.STATIC_ROOT}
))

urlpatterns += patterns('',
               (r'^media/(?P<path>.*)$', 'django.views.static.serve',
                 {'document_root': settings.MEDIA_ROOT}),
              )