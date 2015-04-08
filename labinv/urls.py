from django.conf.urls import patterns,url
from labinv import views
from django.contrib.auth.decorators import login_required

# To use url tag in template, use something like {% url 'labinv:URLNAME' %}
urlpatterns = patterns('',
	# url(r'accounts/login/', 'django.contrib.auth.views.login'),
	url(r'^$', views.index, name='index'),
	url(r'^gRNA/$', views.gRNAList, name='gRNA-list'),
	url(r'^gRNA/create$', login_required(views.gRNACreateView.as_view()), name='gRNA-create'),
	url(r'^gRNA/(?P<pk>\d+)$',views.gRNADetail, name='gRNA-detail'),
	url(r'^gRNA/(?P<pk>\d+)/update$',login_required(views.gRNAUpdateView.as_view()), name='gRNA-update'),
	url(r'^gRNA/(?P<pk>\d+)/delete$',login_required(views.gRNADeleteView.as_view()), name='gRNA-delete'),
	url(r'^cas9/$', views.cas9List, name='cas9-list'),
	url(r'^cas9/create$', login_required(views.cas9CreateView.as_view()), name='cas9-create'),
	url(r'^cas9/(?P<pk>\d+)$',views.cas9Detail, name='cas9-detail'),
	url(r'^cas9/(?P<pk>\d+)/update$',login_required(views.cas9UpdateView.as_view()), name='cas9-update'),
	url(r'^cas9/(?P<pk>\d+)/delete$',login_required(views.cas9DeleteView.as_view()), name='cas9-delete'),
	url(r'^strip/$', views.stripList, name='strip-list'),
	url(r'^strip/create$', login_required(views.stripCreateView.as_view()), name='strip-create'),
	url(r'^strip/(?P<pk>\d+)$',views.stripDetail, name='strip-detail'),
	url(r'^strip/(?P<pk>\d+)/update$',login_required(views.stripUpdateView.as_view()), name='strip-update'),
	url(r'^strip/(?P<pk>\d+)/delete$',login_required(views.stripDeleteView.as_view()), name='strip-delete'),
	url(r'^tube/$', views.tubeList, name='tube-list'),
	url(r'^tube/create$', login_required(views.tubeCreateView.as_view()), name='tube-create'),
	url(r'^tube/(?P<pk>\d+)$',views.tubeDetail, name='tube-detail'),
	url(r'^tube/(?P<pk>\d+)/update$',login_required(views.tubeUpdateView.as_view()), name='tube-update'),
	url(r'^tube/(?P<pk>\d+)/delete$',login_required(views.tubeDeleteView.as_view()), name='tube-delete'),
	)