from django.db import models
from polymorphic import PolymorphicModel
import datetime
from django.core.urlresolvers import reverse

# Create your models here.
class Experiment(PolymorphicModel):
	# shortName=models.CharField(max_length=50)
	date=models.DateField('Date; if in doubt, end date',default=datetime.date.today())
	note=models.TextField()
	def __str__(self):
		dateString=datetime.date.strftime(self.date,'%m%d%y')
		return dateString+'_exp'

class uInjection(Experiment):
	gRNA=models.ForeignKey('labinv.gRNA',related_name='inxgRNA')
	gRNAvolume=models.DecimalField('volume in uL',max_digits=3,decimal_places=2,default=1.0)
	cas9=models.ForeignKey('labinv.cas9',related_name='inxcas9')
	cas9volume=models.DecimalField('volume in uL',max_digits=3,decimal_places=2,default=1.0)
	otherTubes=models.ManyToManyField('labinv.Tube',blank=True,null=True)
	totalVol=models.DecimalField('total volume in uL',max_digits=3,decimal_places=2)
	injectVol=models.DecimalField('injected volume in nL',max_digits=2,decimal_places=1)
	strain=models.CharField('which strain of fish were injected',max_length=20)
	def __str__(self):
		dateString=datetime.date.strftime(self.date,'%m%d%y')
		return dateString+'_uInx_'+self.gRNA.geneTarget
	# def get_absolute_url(self):
	# 	return reverse('data.views.uInx-detail',args=[str(self.id)])

class inxSurvivalExp(Experiment):
	inx=models.OneToOneField('uInjection')
	nInx=models.IntegerField('Number injected',default=100)
	dailyDeathsExp=models.CommaSeparatedIntegerField('Experimental group deaths, comma separated',
		default='0,0,0,0,0,0,0,0',max_length=100)
	# expFinalSurviving=models.IntegerField('Experimental larvae surviving at 7 dpf',default=0)
	nCtrl=models.IntegerField('Number of control embryos',default=300)
	dailyDeathsCtrl=models.CommaSeparatedIntegerField('Control group deaths, comma separated',
		default='0,0,0,0,0,0,0,0',max_length=100)
	# ctrlFinalSurviving=models.IntegerField('Control larvae surviving at 7 dpf',default=0)
	ctrlType=models.CharField('Control type: uninjected vs sham or cas9 injected, etc.',max_length=20)
	def __str__(self):	
		dateString=datetime.date.strftime(self.date,'%m%d%y')
		return dateString+'_inxSurvival_'+self.inx.gRNA.geneTarget
	# def get_absolute_url(self):
	# 	return reverse('data.views.survExp-detail',args=[str(self.id)])

class survivalExp(Experiment):
	shortName=models.CharField(max_length=50)
	nExp=models.IntegerField('Number injected',default=100)
	dailyDeathsExp=models.CommaSeparatedIntegerField('Experimental group deaths, comma separated',
		default='0,0,0,0,0,0,0,0',max_length=100)
	# expFinalSurviving=models.IntegerField('Experimental larvae surviving at 7 dpf',default=0)
	def __str__(self):	
		dateString=datetime.date.strftime(self.date,'%m%d%y')
		return dateString+'_survival_'+self.shortName

class miscExp(Experiment):
	# No idea what this might be for, but it may come in handy.
	shortName=models.CharField(max_length=50)
	# def get_absolute_url(self):
	# 	return reverse('data.views.miscExp-detail',args=[str(self.id)])

class fileData(PolymorphicModel):
	shortName=models.CharField(max_length=50)
	date=models.DateField(default=datetime.date.today())
	note=models.TextField()
	# IMG_TYPES=(
	# 	('gel','gel'),
	# 	('misc','misc'),
	# 	)
	# imgType=models.CharField(choices=IMG_TYPES,max_length=10)
	# def get_imgType(self):
	# 	return self.imgType
	
	def __str__(self):
		dateString=datetime.date.strftime(self.date,'%m%d%y')
		return dateString+'_file_'+self.shortName

class gel(fileData):
	exp=models.ForeignKey(Experiment)	# an image should belong to the inx or misc experiment, not to survival, unless needed to show monsters
	# exp is a fkey and not a manytomany for simplicity. When an image refers to more than one experiment, it should be cropped to refer to only
	# one, or simply uploaded multiple times, once for each fkey experiment.
	final=models.BooleanField(default=False)	# note: ONLY to be used for T7E1, or other standardized files
	key=models.TextField('Key; comma-separated by lane; semicolon separated for multiple rows')	# add "only one semicolon" validator
	tubes=models.ManyToManyField('labinv.Tube',blank=True,null=True)
	gelFile=models.ImageField(upload_to='images/gels/')
	# def get_absolute_url(self):
	# 	return reverse('data.views.gel-detail',args=[str(self.id)])
	def __str__(self):
		dateString=datetime.date.strftime(self.date,'%m%d%y')
		return dateString+'_gel_'+self.shortName

class miscImg(fileData):
	exp=models.ForeignKey(Experiment)
	# This is for scope images and the like.
	imgFile=models.ImageField(upload_to='images/misc/')
	# def get_absolute_url(self):
	# 	return reverse('data.views.miscImg-detail',args=[str(self.id)])
	def __str__(self):
		dateString=datetime.date.strftime(self.date,'%m%d%y')
		return dateString+'_img_'+self.shortName

class miscFile(fileData):
	exp=models.ForeignKey(Experiment)
	final=models.BooleanField(default=False)	# note: ONLY to be used for expInfo phenotype, or other standardized files
	# This is for csvs or mat files pertaining to experiments
	userFile=models.FileField(upload_to='files/')