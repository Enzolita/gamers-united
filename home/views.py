from django.shortcuts import render

from django.views.generic import TemplateView
from django.http import HttpResponse


# Create your views here.

class Index(TemplateView):
    template_name = 'home/index.html'

class About(TemplateView):
    template_name = 'home/about.html'    
    def about(request):
     return render(request, "about.html")