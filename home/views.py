from django.shortcuts import render

from django.views.generic import TemplateView



# Create your views here.

class Index(TemplateView):
    template_name = 'home/index.html'

class About(TemplateView):
    template_name = 'home/about.html'    
    def about(request):
     return render(request, "about.html")

class Posts(TemplateView):
    template_name = 'posts/index.html'    
    def about(request):
     return render(request, "index.html")