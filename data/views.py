from django.shortcuts import render
from django.http import HttpResponse
from django.template import Context, loader

from django.views.generic import CreateView,UpdateView,DeleteView,TemplateView

from .models import *
from .forms import *

from django.contrib.auth.decorators import login_required 

# Create your views here.

@login_required
def index(request):
	t = loader.get_template('data/dataindex.html')
	C=Context()
	return HttpResponse(t.render(C))

###################################################################################################

# Experiments

###################################################################################################

################################
# inxSurvival Experiment views #
################################

@login_required
def inxSurvExpList(request):
	t=loader.get_template('data/inxSurvExpList.html')
	inxSurvExps=inxSurvivalExp.objects.all()
	C=Context({'inxSurvExps': inxSurvExps})
	# consider calculating additional context variables in the future, for utility, such as survival %s
	return HttpResponse(t.render(C))
	
class inxSurvExpCreateView(CreateView):
    model = inxSurvivalExp
    success_url='/data/inxSurvExp/'

class inxSurvExpUpdateView(UpdateView):
	model = inxSurvivalExp
	success_url='/data/inxSurvExp/'

class inxSurvExpDeleteView(DeleteView):
	model = survivalExp
	success_url='/data/inxSurvExp/'

@login_required
def inxSurvExpPlot(request,pk):
	import random
	import django
	import pandas as pd
	from re import split
	from lifelines.utils import survival_events_from_table
	from lifelines import KaplanMeierFitter
	from matplotlib.backends.backend_agg import FigureCanvasAgg as FigureCanvas
	from matplotlib.figure import Figure

	thisinxSurvExp=inxSurvivalExp.objects.get(pk=pk)
	# without wasting variables, this converts the comma-separated string into an int list
	dailyDeathsExp=[int(deathExp) for deathExp in split(',',thisinxSurvExp.dailyDeathsExp)]
	expFinalSurviving=thisinxSurvExp.nInx-sum(dailyDeathsExp)
	dailyDeathsExp.append(expFinalSurviving)
	dailyDeathsCtrl=[int(deathCtrl) for deathCtrl in split(',',thisinxSurvExp.dailyDeathsCtrl)]
	ctrlFinalSurviving=thisinxSurvExp.nCtrl-sum(dailyDeathsCtrl)
	dailyDeathsCtrl.append(ctrlFinalSurviving)
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
	ax=kmfExp.fit(Texp,event_observed=Cexp,label=thisinxSurvExp.inx.gRNA.geneTarget+' injected\nn = '+str(thisinxSurvExp.nInx)).plot(ax=ax)

	kmfCtrl=KaplanMeierFitter()
	ax=kmfCtrl.fit(Tctrl,event_observed=Cctrl,label=thisinxSurvExp.ctrlType+'\nn = '+str(thisinxSurvExp.nCtrl)).plot(ax=ax)
	ax.set_ylabel('Fraction Surviving')
	ax.set_xlabel('Days post-fertilization')

	canvas=FigureCanvas(fig)
	response=HttpResponse(content_type='image/png')
	canvas.print_png(response)
	return response	

@login_required
def inxSurvExpDetail(request,pk):
	t=loader.get_template('data/inxsurvexpdetail.html')
	thisinxSurvExp=survivalExp.objects.get(pk=pk)
	C=Context({'inxSurvExp': thisinxSurvExp})
	return HttpResponse(t.render(C))

#############################
# Survival Experiment views #
#############################

@login_required
def survExpList(request):
	t=loader.get_template('data/survExpList.html')
	survExps=survivalExp.objects.all()
	C=Context({'survExps': survExps})
	return HttpResponse(t.render(C))
	
class survExpCreateView(CreateView):
    model = survivalExp
    success_url='/data/survExp/'

class survExpUpdateView(UpdateView):
	model = survivalExp
	success_url='/data/survExp/'

class survExpDeleteView(DeleteView):
	model = survivalExp
	success_url='/data/survExp/'

@login_required
def survExpPlot(request,pk):
	import random
	import django
	import pandas as pd
	from re import split
	from lifelines.utils import survival_events_from_table
	from lifelines import KaplanMeierFitter
	from matplotlib.backends.backend_agg import FigureCanvasAgg as FigureCanvas
	from matplotlib.figure import Figure

	thisSurvExp=survivalExp.objects.get(pk=pk)
	# without wasting variables, this converts the comma-separated string into an int list
	dailyDeathsExp=[int(deathExp) for deathExp in split(',',thisSurvExp.dailyDeathsExp)]
	expFinalSurviving=thisinxSurvExp.nExp-sum(dailyDeathsExp)
	dailyDeathsExp.append(expFinalSurviving)
	# we need a way for lifelines to understand that not all of our fish died by 7dpf, so we use the 
	# censorship parameter to say that the last element in this list represents the number of surviving 
	# fish for the experiment.
	censorHack=[0]*(len(dailyDeathsExp)-1)
	censorHack.append(1)

	expSurvival=pd.DataFrame({'Texp':dailyDeathsExp,'Cexp':censorHack})
	Texp,Cexp=survival_events_from_table(expSurvival,observed_deaths_col='Texp',censored_col='Cexp')

	# plotting to image happens here.
	fig=Figure()
	ax=fig.add_subplot(111)

	kmfExp=KaplanMeierFitter()
	ax=kmfExp.fit(Texp,event_observed=Cexp,label=str(thisSurvExp)+'\nn = '+thisSurvExp.nExp).plot(ax=ax)
	ax.set_ylabel('Fraction Surviving')

	canvas=FigureCanvas(fig)
	response=HttpResponse(content_type='image/png')
	canvas.print_png(response)
	return response	

@login_required
def survExpDetail(request,pk):
	t=loader.get_template('data/survexpdetail.html')
	thisSurvExp=survivalExp.objects.get(pk=pk)
	C=Context({'survExp': thisSurvExp})
	return HttpResponse(t.render(C))

###############################
# uInjection Experiment views #
###############################

@login_required
def uInxList(request):
	t=loader.get_template('data/uinxlist.html')
	uInjections=uInjection.objects.all()
	C=Context({'uInjections': uInjections})
	return HttpResponse(t.render(C))

class uInxCreateView(CreateView):
    model = uInjection
    success_url='/data/uInx/'

class uInxUpdateView(UpdateView):
	model = uInjection
	success_url='/data/uInx/'

class uInxDeleteView(DeleteView):
	model = uInjection
	success_url='/data/uInx/'

@login_required
def uInxDetail(request,pk):
	t=loader.get_template('data/uinxdetail.html')
	thisUInx=survivalExp.objects.get(pk=pk)
	C=Context({'uInx': thisUInx})
	return HttpResponse(t.render(C))
    
########################
# miscExperiment views #
########################

def miscExpList(request):
	t=loader.get_template('data/miscExpList.html')
	miscExps=miscExp.objects.all()
	C=Context({'miscExps': miscExps})
	return HttpResponse(t.render(C))

class miscExpCreateView(CreateView):
    model = miscExp
    success_url='/data/exp/'

class miscExpUpdateView(UpdateView):
	model = miscExp
	success_url='/data/exp/'

class miscExpDeleteView(DeleteView):
	model = miscExp
	success_url='/data/exp/'

@login_required
def miscExpDetail(request,pk):
	t=loader.get_template('data/miscexpdetail.html')
	thisMiscExp=miscExp.objects.get(pk=pk)
	C=Context({'miscExp': thisMiscExp})
	return HttpResponse(t.render(C))

###################################################################################################

# Images and other Files

###################################################################################################

#############
# gel views #
#############

def gelList(request):
	t=loader.get_template('data/gelList.html')
	gels=gel.objects.all()
	C=Context({'gels': gels})
	return HttpResponse(t.render(C))

class gelCreateView(CreateView):
    model = gel
    success_url='/data/gel/'

class gelUpdateView(UpdateView):
	model = gel
	success_url='/data/gel/'

class gelDeleteView(DeleteView):
	model = gel
	success_url='/data/gel/'

@login_required
def gelDetail(request,pk):
	t=loader.get_template('data/geldetail.html')
	thisGel=gel.objects.get(pk=pk)
	C=Context({'gel': thisGel})
	return HttpResponse(t.render(C))

#################
# miscImg views #
#################

def miscImgList(request):
	t=loader.get_template('data/miscImgList.html')
	miscImgs=miscImg.objects.all()
	C=Context({'miscImgs': miscImgs})
	return HttpResponse(t.render(C))

class miscImgCreateView(CreateView):
    form_class = ImgUploadModelForm
    template_name = 'data/miscimg_form.html'
    success_url='/data/img/'

class miscImgUpdateView(UpdateView):
	model = miscImg
	success_url='/data/img/'

class miscImgDeleteView(DeleteView):
	model = miscImg
	success_url='/data/img/'

@login_required
def miscImgDetail(request,pk):
	t=loader.get_template('data/miscImgdetail.html')
	thisMiscImg=miscImg.objects.get(pk=pk)
	C=Context({'miscImg': thisMiscImg})
	return HttpResponse(t.render(C))

##################
# miscFile views #
##################

def miscFileList(request):
	t=loader.get_template('data/miscFileList.html')
	miscFiles=miscFile.objects.all()
	C=Context({'miscFiles': miscFiles})
	return HttpResponse(t.render(C))

class miscFileCreateView(CreateView):
    model = miscFile
    success_url='/data/file/'

class miscFileUpdateView(UpdateView):
	model = miscFile
	success_url='/data/file/'

class miscFileDeleteView(DeleteView):
	model = miscFile
	success_url='/data/file/'

@login_required
def miscFileDetail(request,pk):
	t=loader.get_template('data/miscfiledetail.html')
	thisMiscFile=miscFile.objects.get(pk=pk)
	C=Context({'miscFile': thisMiscFile})
	return HttpResponse(t.render(C))