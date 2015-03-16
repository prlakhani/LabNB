from django.contrib import admin
from polymorphic.admin import PolymorphicParentModelAdmin, PolymorphicChildModelAdmin
from data.models import Experiment,uInjection,survivalExp,miscExp,imgData,gel,miscImg

# Register your models here.

# Start by subclassing polymorphic models - see the readthedocs

class ExperimentChildAdmin(PolymorphicChildModelAdmin):
	base_model = Experiment

class uInjectionAdmin(ExperimentChildAdmin):
	pass

class survivalExpAdmin(ExperimentChildAdmin):
	pass

class miscExpAdmin(ExperimentChildAdmin):
	pass

class ExperimentParentAdmin(PolymorphicParentModelAdmin):
	base_model = Experiment
	child_models = (
		(uInjection,uInjectionAdmin),
		(survivalExp,survivalExpAdmin),
		(miscExp,miscExpAdmin),
	)

class imgDataChildAdmin(PolymorphicChildModelAdmin):
	base_model = imgData

class gelAdmin(imgDataChildAdmin):
	pass

class miscImgAdmin(imgDataChildAdmin):
	pass

class imgDataParentAdmin(PolymorphicParentModelAdmin):
	base_model = imgData
	child_models = (
		(gel,gelAdmin),
		(miscImg,miscImgAdmin),
	)
# now actually register the parent

admin.site.register(Experiment, ExperimentParentAdmin)
admin.site.register(imgData, imgDataParentAdmin)