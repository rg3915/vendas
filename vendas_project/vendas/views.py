# coding: utf-8
from django.views.generic import TemplateView, ListView

class index(TemplateView):
	template_name = 'index.html'

class sobre(TemplateView):
	template_name = 'sobre.html'
