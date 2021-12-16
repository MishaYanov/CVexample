from django.shortcuts import render
from django.views.generic import TemplateView, ListView, DetailView, CreateView, UpdateView,DeleteView


# Create your views here.
class HomePage(TemplateView):
    template_name = 'index.html'
    
class Certificates(TemplateView):
    template_name = 'certificates.html'
    
class CoverLetter(TemplateView):
    template_name = 'coverletter.html'