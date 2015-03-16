from django.db import models
from polymorphic import PolymorphicModel
import datetime

# Create your models here.
class Tube(PolymorphicModel):
	shortName=models.CharField(max_length=50)
	date=models.DateField(default=datetime.date.today())
	exists=models.BooleanField(default=True)
	note=models.TextField()
	# class Meta:
	# 	ordering=['date']
	def __str__(self):
		dateString=datetime.date.strftime(self.date,'%m%d%y')
		return dateString+'_'+self.shortName

class gRNA(Tube):
	geneTarget=models.CharField(max_length=10)
	targetSeq=models.CharField(max_length=30)
	PROMOTER_CHOICES=(
		('T7','T7'),
		('SP6','SP6')
		)
	promoter=models.CharField(choices=PROMOTER_CHOICES,max_length=10)
	concentration=models.FloatField('concentration in ng/uL')
	def __str__(self):
		dateString=datetime.date.strftime(self.date,'%m%d%y')
		return dateString+'_'+self.geneTarget

class cas9(Tube):
	TYPE_CHOICES=(
		('mRNA','mRNA'),
		('protein','protein')
		)
	c9type=models.CharField(choices=TYPE_CHOICES,max_length=10)
	concentration=models.FloatField('concentration in ng/uL')
	def __str__(self):
		dateString=datetime.date.strftime(self.date,'%m%d%y')
		return dateString+'_'+self.c9type

class strip(Tube):
	key=models.TextField('Comma-separated by tube; semicolon if >1 in set')

class miscTube(Tube):
	pass