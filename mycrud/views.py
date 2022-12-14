from multiprocessing import context
from re import template
from django.shortcuts import render
from posts.views import *

def index(request):
    template_name = 'index.html'
    
    context = {
        'title' : 'HOME',
    }
    return render(request, template_name, context)

def about(request):
    template_name = 'about.html'
    context = {
        'title' : 'ABOUT',
    }
    return render(request, template_name, context)