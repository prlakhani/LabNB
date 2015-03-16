from django.conf.urls import patterns,url
from data import views

urlpatterns = patterns('',
	# url(r'^$', views.index, name='index'),
	url(r'^survExp/create$', views.SurvivalExpCreateView.as_view(), name='survExp-create'),
	url(r'^survExpList$', views.survExpList, name='survExpList'),
	url(r'^survExp/(?P<survexp_id>\w+)$'), views.survExpDetail, name='survExpDetail'),
	url(r'^uInx/create$', views.uInjectionCreateView.as_view(), name='uinx-create'),
	url(r'^uInxList$', views.uInxList, name='uinxlist'),
	)