from django.views import defaults
from django.shortcuts import render
from django.http import HttpResponse
from django.template import Context, loader
from django.contrib.auth.decorators import login_required

def page_not_found(request):
	"""Handle the server_error view"""
	return defaults.page_not_found(request, template_name='404.html')

def server_error(request):
	"""Handle the server_error view"""
	return defaults.server_error(request, template_name='500.html')

@login_required
def index(request):
	t = loader.get_template('index.html')
	C=Context()
	return HttpResponse(t.render(C))