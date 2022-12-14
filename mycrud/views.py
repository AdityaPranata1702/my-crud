from multiprocessing import context
from re import template
from django.shortcuts import render
from posts.views import *

def index(request):
    template_name = 'index.html'
    posting_list = Posting.objects.all()
    context = {
        'title' : 'Halaman Pertama',
        'posting' : posting_list,
    }
    return render(request, template_name, context)

def about(request):
    template_name = 'about.html'
    context = {
        'title' : 'Halaman Ketiga'
    }
    return render(request, template_name, context)