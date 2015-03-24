from django.conf.urls import patterns,url
from data import views

urlpatterns = patterns('',
	url(r'^$', views.index, name='index'),
	url(r'^inxSurvExp/$', views.inxSurvExpList, name='inxSurvExp-list'),
	url(r'^inxSurvExp/create$', views.inxSurvExpCreateView.as_view(), name='inxSurvExp-create'),
	url(r'^inxSurvExp/(?P<pk>\d+)/inxsurvplot.png$', views.inxSurvExpPlot, name='inxSurvExp-Plot'),
	url(r'^inxSurvExp/(?P<pk>\d+)$', views.inxSurvExpDetail, name='inxSurvExp-detail'),
	url(r'^inxSurvExp/(?P<pk>\d+)/update$', views.inxSurvExpUpdateView.as_view(), name='inxSurvExp-update'),
	url(r'^inxSurvExp/(?P<pk>\d+)/delete$', views.inxSurvExpDeleteView.as_view(), name='inxSurvExp-delete')
	url(r'^survExp/$', views.survExpList, name='survExp-list'),
	url(r'^survExp/create$', views.survExpCreateView.as_view(), name='survExp-create'),
	url(r'^survExp/(?P<pk>\d+)/survplot.png$', views.survExpPlot, name='survExp-Plot'),
	url(r'^survExp/(?P<pk>\d+)$', views.survExpDetail, name='survExp-detail'),
	url(r'^survExp/(?P<pk>\d+)/update$', views.survExpUpdateView.as_view(), name='survExp-update'),
	url(r'^survExp/(?P<pk>\d+)/delete$', views.survExpDeleteView.as_view(), name='survExp-delete')
	url(r'^uInx/$', views.uInxList, name='uinx-list'),
	url(r'^uInx/create$', views.uInxCreateView.as_view(), name='uInx-create'),
	url(r'^uInx/(?P<pk>\d+)$', views.uInxDetail, name='uInx-detail'),
	url(r'^uInx/(?P<pk>\d+)/update$', views.uInxUpdateView.as_view(), name='uInx-update'),
	url(r'^uInx/(?P<pk>\d+)/delete$', views.uInxDeleteView.as_view(), name='uInx-delete'),
	)

urlpatterns += patterns('', (
        r'^static/(?P<path>.*)$',
        'django.views.static.serve',
        {'document_root': settings.STATIC_ROOT}
))