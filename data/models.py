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
	gRNA=models.ForeignKey('labinv.gRNA',related_name='gRNA')
	gRNAvolume=models.DecimalField('volume in uL',max_digits=3,decimal_places=2,default=1.0)
	cas9=models.ForeignKey('labinv.cas9',related_name='cas9')
	cas9volume=models.DecimalField('volume in uL',max_digits=3,decimal_places=2,default=1.0)
	otherTubes=models.ManyToManyField('labinv.Tube',blank=True,null=True)
	totalVol=models.DecimalField('total volume in uL',max_digits=3,decimal_places=2)
	injectVol=models.DecimalField('injected volume in nL',max_digits=2,decimal_places=1)
	def __str__(self):
		dateString=datetime.date.strftime(self.date,'%m%d%y')
		return dateString+'_'+self.gRNA
	def get_absolute_url(self):
		return reverse('data.views.uInx-detail',args=[str(self.id)])

class survivalExp(Experiment):
	inx=models.ForeignKey(uInjection)
	nInx=models.IntegerField('Number injected',default=100)
	dailyDeathsExp=models.CommaSeparatedIntegerField('Experimental group deaths, comma separated',
		default='0,0,0,0,0,0,0,0',max_length=100)
	expFinalSurviving=models.IntegerField('Experimental larvae surviving at 7 dpf',default=0)
	nCtrl=models.IntegerField('Number of control embryos',default=300)
	dailyDeathsCtrl=models.CommaSeparatedIntegerField('Control group deaths, comma separated',
		default='0,0,0,0,0,0,0,0',max_length=100)
	ctrlFinalSurviving=models.IntegerField('Control larvae surviving at 7 dpf',default=0)
	ctrlType=models.CharField('uninjected or untreated, sham or cas9 injected, etc.',max_length=20)
	def __str__(self):	
		dateString=datetime.date.strftime(self.date,'%m%d%y')
		return dateString+'_inxSurvival_'+self.inx.gRNA
	def get_absolute_url(self):
		return reverse('data.views.survExp-detail',args=[str(self.id)])

class miscExp(Experiment):
	pass
	def get_absolute_url(self):
		return reverse('data.views.miscExp-detail',args=[str(self.id)])

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
	def get_absolute_url(self):
		return reverse('data.views.gel-detail',args=[str(self.id)])

class miscImg(imgData):
	def get_absolute_url(self):
		return reverse('data.views.miscImg-detail',args=[str(self.id)])