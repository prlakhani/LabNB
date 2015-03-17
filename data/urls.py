from django.conf.urls import patterns,url
from data import views

urlpatterns = patterns('',
	# url(r'^$', views.index, name='index'),
	url(r'^survExp$', views.survExpList, name='survExp-list'),
	url(r'^survExp/create$', views.SurvivalExpCreateView.as_view(), name='survExp-create'),
	url(r'^survExp/(?P<survexp_id>\d+)$'), views.survExpDetail, name='survExp-detail'),

	url(r'^uInxList$', views.uInxList, name='uinx-list'),
	url(r'^uInx/create$', views.uInxCreateView.as_view(), name='uInx-create'),
	url(r'^uInx/(?P<uInx_id>\d+)$'), views.uInxDetail, name='uInx-detail'),
	url(r'^uInx/update(?P<uInx_id>\d+)$', views.uInxUpdateView.as_view(), name='uInx-update'),
	
	)