from multiprocessing import context
from re import template
from django.shortcuts import render
from posts.views import *

def index(request):
    template_name = 'index.html'
    url = "https://api-berita-indonesia.vercel.app/antara/tekno/"
    
    api = requests.get(url).json()
    a = api['data']
    title=[]
    content=[]
    image = []
    
    for i in range(len(a)):
        f = a[i]
        title.append(f['title'])
        content.append(f['description'])
        image.append(f['image'])
        
    mylist = zip(title, content, image)
    context = {
        'title' : 'HOME',
        'mylist' : mylist,
    }
    return render(request, template_name, context)

def about(request):
    template_name = 'about.html'
    context = {
        'title' : 'ABOUT',
    }
    return render(request, template_name, context)