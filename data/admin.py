from django.contrib import admin
from polymorphic.admin import PolymorphicParentModelAdmin, PolymorphicChildModelAdmin
from data.models import Experiment,uInjection,survivalExp,miscExp,fileData,gel,miscImg,miscFile

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

class fileDataChildAdmin(PolymorphicChildModelAdmin):
	base_model = fileData

class gelAdmin(fileDataChildAdmin):
	pass

class miscImgAdmin(fileDataChildAdmin):
	pass


class miscFileAdmin(fileDataChildAdmin):
	pass

class fileDataParentAdmin(PolymorphicParentModelAdmin):
	base_model = fileData
	child_models = (
		(gel,gelAdmin),
		(miscImg,miscImgAdmin),
		(miscFile,miscFileAdmin),
	)
# now actually register the parent

admin.site.register(Experiment, ExperimentParentAdmin)
admin.site.register(fileData, fileDataParentAdmin)