from django.db import models
from polymorphic import PolymorphicModel
import datetime
from django.core.urlresolvers import reverse

# Create your models here.
class Tube(PolymorphicModel):
	# shortName=models.CharField(max_length=50)
	date=models.DateField(default=datetime.date.today())
	exists=models.BooleanField(default=True)
	note=models.TextField()
	# class Meta:
	# 	ordering=['date']
	def __str__(self):
		dateString=datetime.date.strftime(self.date,'%m%d%y')
		return dateString+'_tube'

class gRNA(Tube):
	geneTarget=models.CharField(max_length=10)
	targetSeq=models.CharField(max_length=30)
	PROMOTER_CHOICES=(
		('T7','T7'),
		('SP6','SP6')
		)
	promoter=models.CharField(choices=PROMOTER_CHOICES,max_length=10)
	concentration=models.FloatField('concentration in ng/uL')
	primerF=models.OneToOneField('miscTube',related_name='primerF',blank=True,null=True)
	primerR=models.OneToOneField('miscTube',related_name='primerR',blank=True,null=True)
	prodSize=models.IntegerField('PCR product size for these primers',default=300,blank=True,null=True)
	def __str__(self):
		dateString=datetime.date.strftime(self.date,'%m%d%y')
		return dateString+'_gRNA_'+self.geneTarget
	# @models.permalink
	# def get_absolute_url(self):
	# 	return reverse('labinv.views.gRNA-detail',args=[str(self.id)])

class cas9(Tube):
	TYPE_CHOICES=(
		('mRNA','mRNA'),
		('protein','protein')
		)
	c9type=models.CharField(choices=TYPE_CHOICES,max_length=10)
	concentration=models.FloatField('concentration in ng/uL')
	def __str__(self):
		dateString=datetime.date.strftime(self.date,'%m%d%y')
		return dateString+'_cas9'+self.c9type
	# @models.permalink
	# def get_absolute_url(self):
	# 	return reverse('labinv.views.cas9-detail',args=[str(self.id)])

class strip(Tube):
	shortName=models.CharField(max_length=50)
	key=models.TextField('Key; comma-separated by tube; semicolon if >1 in set')
	# @models.permalink
	# def get_absolute_url(self):
	# 	return reverse('labinv.views.strip-detail',args=[str(self.id)])
	def __str__(self):
		dateString=datetime.date.strftime(self.date,'%m%d%y')
		return dateString+'_strip_'+self.shortName

class miscTube(Tube):
	shortName=models.CharField(max_length=50)
	sequence=models.CharField('Sequence, if applicable (primers)',max_length=200,blank=True,null=True)
	def __str__(self):
		dateString=datetime.date.strftime(self.date,'%m%d%y')
		return dateString+'_tube_'+self.shortName
	# @models.permalink
	# def get_absolute_url(self):
	# 	return reverse('labinv.views.miscTube-detail',args=[str(self.id)])