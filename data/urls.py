from django.conf.urls import patterns,url
from data import views
from django.conf import settings
from django.contrib.auth.decorators import login_required

# To use url tag in template, use something like {% url 'data:URLNAME' %}

urlpatterns = patterns('',
	# url(r'accounts/login/', 'django.contrib.auth.views.login'),
	url(r'^$', views.index, name='index'),
	url(r'^inxSurvExp/$', views.inxSurvExpList, name='inxSurvExp-list'),
	url(r'^inxSurvExp/create$', login_required(views.inxSurvExpCreateView.as_view()), name='inxSurvExp-create'),
	url(r'^inxSurvExp/(?P<pk>\d+)/inxsurvplot.png$', views.inxSurvExpPlot, name='inxSurvExp-plot'),
	url(r'^inxSurvExp/(?P<pk>\d+)$', views.inxSurvExpDetail, name='inxSurvExp-detail'),
	url(r'^inxSurvExp/(?P<pk>\d+)/update$', login_required(views.inxSurvExpUpdateView.as_view()), name='inxSurvExp-update'),
	url(r'^inxSurvExp/(?P<pk>\d+)/delete$', login_required(views.inxSurvExpDeleteView.as_view()), name='inxSurvExp-delete'),
	url(r'^survExp/$', views.survExpList, name='survExp-list'),
	url(r'^survExp/create$', login_required(views.survExpCreateView.as_view()), name='survExp-create'),
	url(r'^survExp/(?P<pk>\d+)/survplot.png$', views.survExpPlot, name='survExp-plot'),
	url(r'^survExp/(?P<pk>\d+)$', views.survExpDetail, name='survExp-detail'),
	url(r'^survExp/(?P<pk>\d+)/update$', login_required(views.survExpUpdateView.as_view()), name='survExp-update'),
	url(r'^survExp/(?P<pk>\d+)/delete$', login_required(views.survExpDeleteView.as_view()), name='survExp-delete'),
	url(r'^uInx/$', views.uInxList, name='uInx-list'),
	url(r'^uInx/create$', login_required(views.uInxCreateView.as_view()), name='uInx-create'),
	url(r'^uInx/(?P<pk>\d+)$', views.uInxDetail, name='uInx-detail'),
	url(r'^uInx/(?P<pk>\d+)/update$', login_required(views.uInxUpdateView.as_view()), name='uInx-update'),
	url(r'^uInx/(?P<pk>\d+)/delete$', login_required(views.uInxDeleteView.as_view()), name='uInx-delete'),
	url(r'^exp/$', views.miscExpList, name='exp-list'),
	url(r'^exp/create$', login_required(views.miscExpCreateView.as_view()), name='exp-create'),
	url(r'^exp/(?P<pk>\d+)$', views.miscExpDetail, name='exp-detail'),
	url(r'^exp/(?P<pk>\d+)/update$', login_required(views.miscExpUpdateView.as_view()), name='exp-update'),
	url(r'^exp/(?P<pk>\d+)/delete$', login_required(views.miscExpDeleteView.as_view()), name='exp-delete'),
	url(r'^gel/$', views.gelList, name='gel-list'),
	url(r'^gel/create$', login_required(views.gelCreateView.as_view()), name='gel-create'),
	url(r'^gel/(?P<pk>\d+)$', views.gelDetail, name='gel-detail'),
	url(r'^gel/(?P<pk>\d+)/update$', login_required(views.gelUpdateView.as_view()), name='gel-update'),
	url(r'^gel/(?P<pk>\d+)/delete$', login_required(views.gelDeleteView.as_view()), name='gel-delete'),
	url(r'^img/$', views.miscImgList, name='img-list'),
	url(r'^img/create$', login_required(views.miscImgCreateView.as_view()), name='img-create'),
	url(r'^img/(?P<pk>\d+)$', views.miscImgDetail, name='img-detail'),
	url(r'^img/(?P<pk>\d+)/update$', login_required(views.miscImgUpdateView.as_view()), name='img-update'),
	url(r'^img/(?P<pk>\d+)/delete$', login_required(views.miscImgDeleteView.as_view()), name='img-delete'),
	url(r'^file/$', views.miscFileList, name='file-list'),
	url(r'^file/create$', login_required(views.miscFileCreateView.as_view()), name='file-create'),
	url(r'^file/(?P<pk>\d+)$', views.miscFileDetail, name='file-detail'),
	url(r'^file/(?P<pk>\d+)/update$', login_required(views.miscFileUpdateView.as_view()), name='file-update'),
	url(r'^file/(?P<pk>\d+)/delete$', login_required(views.miscFileDeleteView.as_view()), name='file-delete'),
	url(r'^custom/querydata$',views.queryData,name='querydata'),
	)

urlpatterns += patterns('', (
        r'^static/(?P<path>.*)$',
        'django.views.static.serve',
        {'document_root': settings.STATIC_ROOT}
)
)

urlpatterns += patterns('',
               (r'^media/(?P<path>.*)$', 'django.views.static.serve',
                 {'document_root': settings.MEDIA_ROOT}),
              )