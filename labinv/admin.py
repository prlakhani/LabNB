from django.contrib import admin
from polymorphic.admin import PolymorphicParentModelAdmin, PolymorphicChildModelAdmin
from labinv.models import Tube,gRNA,cas9,strip,miscTube

# Register your models here.

# Start by subclassing polymorphic models - see the readthedocs

class TubeChildAdmin(PolymorphicChildModelAdmin):
	base_model = Tube

class gRNAAdmin(TubeChildAdmin):
	pass

class cas9Admin(TubeChildAdmin):
	pass

class stripAdmin(TubeChildAdmin):
	pass

class miscTubeAdmin(TubeChildAdmin):
	pass

class TubeParentAdmin(PolymorphicParentModelAdmin):
	base_model = Tube
	child_models = (
		(gRNA,gRNAAdmin),
		(cas9,cas9Admin),
		(strip,stripAdmin),
		(miscTube,miscTubeAdmin),
	)

# now actually register the parent

admin.site.register(Tube, TubeParentAdmin)