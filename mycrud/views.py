from multiprocessing import context
from re import template
from django.shortcuts import render
from posts.views import *

def index(request):
    template_name = 'index.html'
    url = "https://newsapi.org/v2/everything?q=Cricket&from=2022-12-14&sortBy=popularity&apiKey=1b15168c2d2f4d15896b3de6b7c8be90"
    
    cricket_news = requests.get(url).json()
    a = cricket_news['articles']
    desc = []
    title = []
    img = []
    
    for i in range(len(a)):
        f = a[i]
        title.append(f['title'])
        desc.append(f['description'])
        img.append(f['urlToImage'])
        
    mylist = zip(title, desc, img)
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