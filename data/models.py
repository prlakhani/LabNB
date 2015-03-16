from django.db import models
from polymorphic import PolymorphicModel
import datetime

# Create your models here.
class Experiment(PolymorphicModel):
	shortName=models.CharField(max_length=50)
	date=models.DateField(default=datetime.date.today())
	note=models.TextField()
	def __str__(self):
		dateString=datetime.date.strftime(self.date,'%m%d%y')
		return dateString+'_'+self.shortName

class uInjection(Experiment):
	gRNA=models.ManyToManyField('labinv.gRNA',related_name='gRNA')
	gRNAvolume=models.DecimalField('volume in uL',max_digits=3,decimal_places=2,default=1.0)
	cas9=models.ForeignKey('labinv.cas9',related_name='cas9')
	cas9volume=models.DecimalField('volume in uL',max_digits=3,decimal_places=2,default=1.0)
	otherTubes=models.ManyToManyField('labinv.Tube',blank=True,null=True)
	totalVol=models.DecimalField('total volume in uL',max_digits=3,decimal_places=2)
	injectVol=models.DecimalField('injected volume in nL',max_digits=2,decimal_places=1)
	def __str__(self):
		dateString=datetime.date.strftime(self.date,'%m%d%y')
		return dateString+'_'+self.gRNA

class survivalExp(Experiment):
	inx=models.ForeignKey(uInjection)
	initPop=models.IntegerField('Initial population')
	dailyDeathsExp=models.CommaSeparatedIntegerField('Experimental group deaths, comma separated',max_length=100)
	dailyDeathsCtrl=models.CommaSeparatedIntegerField('Control group deaths, comma separated',max_length=100)
	ctrlType=models.CharField(max_length=20)
	def __str__(self):
		dateString=datetime.date.strftime(self.date,'%m%d%y')
		return dateString+'_inxSurvival_'+self.uInjection.gRNA

class miscExp(Experiment):
	pass

class imgData(PolymorphicModel):
	shortName=models.CharField(max_length=50)
	date=models.DateField(default=datetime.date.today())
	note=models.TextField()
	IMG_TYPES=(
		('gel','gel'),
		('misc','misc'),
		)
	imgType=models.CharField(choices=IMG_TYPES,max_length=10)
	def get_imgType(self):
		return self.imgType
	imgFile=models.ImageField(upload_to='images/{0}'.format(get_imgType))
	def __str__(self):
		dateString=datetime.date.strftime(self.date,'%m%d%y')
		return dateString+'_'+self.shortName

class gel(imgData):
	key=models.TextField('Comma-separated by lane; semicolon separated for multiple rows')	# add only one semicolon validator
	tubes=models.ManyToManyField('labinv.Tube',blank=True,null=True)

class miscImg(imgData):
	pass