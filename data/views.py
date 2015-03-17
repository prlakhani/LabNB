from django.shortcuts import render
from django.http import HttpResponse
from django.template import Context, loader

from django.views.generic import CreateView,UpdateView,DeleteView,TemplateView

from .models import *

from django.contrib.auth.decorators import login_required 

# Create your views here.

###
# Survival Experiment views
###

def survExpList(request):
	t=loader.get_template('data/survExpList.html')
	survExps=survivalExp.objects.all()
	C=Context({'survExps': survExps})
	return HttpResponse(t.render(C))
	
class survExpCreateView(CreateView):
    model = survivalExp

class survExpUpdateView(UpdateView):
	model = survivalExp

class survExpDeleteView(DeleteView):
	model = survivalExp

def survExpPlot(request,survexp_id):
	import random
	import django
	import pandas as pd
	from re import split
	from lifelines.utils import survival_events_from_table
	from lifelines import KaplanMeierFitter
	from matplotlib.backends.backend_agg import FigureCanvasAgg as FigureCanvas
	from matplotlib.figure import Figure

	thisSurvExp=survivalExp.objects.get(pk=survexp_id)
	# without wasting variables, this converts the comma-separated string into an int list
	dailyDeathsExp=[int(deathExp) for deathExp in split(',',thisSurvExp.dailyDeathsExp)]
	dailyDeathsExp.append(thisSurvExp.expFinalSurviving)
	dailyDeathsCtrl=[int(deathCtrl) for deathCtrl in split(',',thisSurvExp.dailyDeathsCtrl)]
	dailyDeathsCtrl.append(thisSurvExp.ctrlFinalSurviving)
	# we need a way for lifelines to understand that not all of our fish died by 7dpf, so we use the 
	# censorship parameter to say that the last element in this list represents the number of surviving 
	# fish for the experiment.
	censorHack=[0]*(len(dailyDeathsExp)-1)
	censorHack.append(1)

	expSurvival=pd.DataFrame({'Texp':dailyDeathsExp,'Cexp':censorHack})
	Texp,Cexp=survival_events_from_table(expSurvival,observed_deaths_col='Texp',censored_col='Cexp')

	ctrlSurvival=pd.DataFrame({'Tctrl':dailyDeathsCtrl,'Cctrl':censorHack})
	Tctrl,Cctrl=survival_events_from_table(ctrlSurvival,observed_deaths_col='Tctrl',censored_col='Cctrl')

	# plotting to image happens here.
	fig=Figure()
	ax=fig.add_subplot(111)

	kmfExp=KaplanMeierFitter()
	ax=kmfExp.fit(Texp,event_observed=Cexp,label=thisSurvExp.inx.gRNA+' injected\nn = '+thisSurvExp.nInx).plot(ax=ax)

	kmfCtrl=KaplanMeierFitter()
	ax=kmfCtrl.fit(Tctrl,event_observed=Cctrl,label=thisSurvExp.ctrlType+'\nn = '+thisSurvExp.nCtrl).plot(ax=ax)
	ax.set_ylabel('Fraction Surviving')

	canvas=FigureCanvas(fig)
	response=HttpResponse(content_type='image/png')
	canvas.print_png(response)
	return response	
	
def survExpDetail(request,survexp_id):
	t=loader.get_template('data/survexpdetail.html')
	thisSurvExp=survivalExp.objects.get(pk=survexp_id)
	C=Context({'survExp': thisSurvExp})
	return HttpResponse(t.render(C))

###
# uInjection Experiment views
###

def uInxList(request):
	t=loader.get_template('data/uinxlist.html')
	uInjections=uInjection.objects.all()
	C=Context({'uInjections': uInjections})
	return HttpResponse(t.render(C))

class uInxCreateView(CreateView):
    model = uInjection

class uInxUpdateView(UpdateView):
	model = uInjection

class uInxDeleteView(DeleteView):
	model = uInjection
    
