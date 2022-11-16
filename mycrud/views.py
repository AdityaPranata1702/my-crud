from multiprocessing import context
from re import template
from django.shortcuts import render

def index(request):
    template_name = 'index.html'
    context = {
        'title' : 'Halaman Pertama'
    }
    return render(request, template_name, context)

def about(request):
    template_name = 'about.html'
    context = {
        'title' : 'Halaman Ketiga'
    }
    return render(request, template_name, context)