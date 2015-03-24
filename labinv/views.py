from django.shortcuts import render,get_object_or_404
from django.http import HttpResponse
from django.template import Context, loader

from django.views.generic import CreateView,UpdateView,DeleteView

from .models import *

from django.contrib.auth.decorators import login_required

from django.core.urlresolvers import reverse_lazy

# Create your views here.

def index(request):
	t = loader.get_template('labinv/labinvindex.html')
	C=Context()
	return HttpResponse(t.render(C))

def gRNAList(request):
	t=loader.get_template('labinv/gRNAList.html')
	gRNAs=gRNA.objects.all()
	C=Context({'gRNAs': gRNAs})
	return HttpResponse(t.render(C))

class gRNACreateView(CreateView):
    model = gRNA
    success_url='/labinv/gRNA/'
    # def get_object(self):
    # 	return get_object_or_404(gRNA, pk=request.session['pk'])
    # def get_success_url(self):
    # 	return reverse_lazy('gRNA-detail',kwargs={'pk': get_object_or_404().id})

class gRNAUpdateView(UpdateView):
	model = gRNA
	template_name_suffix = '_update_form'
	success_url='/labinv/gRNA/'
	# def get_success_url(self):
	# 	return reverse_lazy('gRNA-detail',kwargs={'pk': self.get_object().id})

class gRNADeleteView(DeleteView):
	model = gRNA
	success_url='/labinv/gRNA/'
	# def get_success_url(self):
	# 	return reverse_lazy('gRNA-list')

def gRNADetail(request,pk):
	t=loader.get_template('labinv/grnadetail.html')
	thisgRNA=gRNA.objects.get(pk=pk)
	C=Context({'gRNA': thisgRNA})
	return HttpResponse(t.render(C))

def cas9List(request):
	t=loader.get_template('labinv/cas9List.html')
	cas9s=cas9.objects.all()
	C=Context({'cas9s': cas9s})
	return HttpResponse(t.render(C))

class cas9CreateView(CreateView):
    model = cas9
    success_url='/labinv/cas9/'

class cas9UpdateView(UpdateView):
	model = cas9
	template_name_suffix = '_update_form'
	success_url='/labinv/cas9/'

class cas9DeleteView(DeleteView):
	model = cas9
	success_url='/labinv/cas9/'

def cas9Detail(request,pk):
	t=loader.get_template('data/cas9detail.html')
	thiscas9=cas9.objects.get(pk=pk)
	C=Context({'cas9': thiscas9})
	return HttpResponse(t.render(C))

def stripList(request):
	t=loader.get_template('labinv/stripList.html')
	strips=strip.objects.all()
	C=Context({'strips': strips})
	return HttpResponse(t.render(C))

class stripCreateView(CreateView):
    model = strip
    success_url='/labinv/strip/'

class stripUpdateView(UpdateView):
	model = strip
	template_name_suffix = '_update_form'
	success_url='/labinv/strip/'

class stripDeleteView(DeleteView):
	model = strip
	success_url='/labinv/strip/'

def stripDetail(request,pk):
	t=loader.get_template('data/stripdetail.html')
	thisstrip=strip.objects.get(pk=pk)
	C=Context({'strip': thisstrip})
	return HttpResponse(t.render(C))

def miscTubeList(request):
	t=loader.get_template('labinv/miscTubeList.html')
	miscTubes=miscTube.objects.all()
	C=Context({'miscTubes': miscTubes})
	return HttpResponse(t.render(C))

class miscTubeCreateView(CreateView):
    model = miscTube
    success_url='/labinv/miscTube/'

class miscTubeUpdateView(UpdateView):
	model = miscTube
	template_name_suffix = '_update_form'
	success_url='/labinv/miscTube/'

class miscTubeDeleteView(DeleteView):
	model = miscTube
	success_url='/labinv/miscTube/'

def miscTubeDetail(request,pk):
	t=loader.get_template('data/miscTubedetail.html')
	thismiscTube=miscTube.objects.get(pk=pk)
	C=Context({'miscTube': thismiscTube})
	return HttpResponse(t.render(C))