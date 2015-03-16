from django.shortcuts import render
from django.http import HttpResponse
from django.template import Context, loader

from django.views.generic import ListView, DetailView,CreateView,TemplateView

from .models import *

from django.contrib.auth.decorators import login_required 

# Create your views here.

class SurvivalExpCreateView(CreateView):
    model = survivalExp

def survExpList(request):
	t=loader.get_template('data/survExpList.html')
	survExps=survivalExp.objects.all()
	C=Context({'survExps': survExps})
	return HttpResponse(t.render(C))

class uInjectionCreateView(CreateView):
    model = uInjection
    
def uInxList(request):
	t=loader.get_template('data/uinxlist.html')
	uInjections=uInjection.objects.all()
	C=Context({'uInjections': uInjections})
	return HttpResponse(t.render(C))