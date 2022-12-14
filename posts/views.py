from django.shortcuts import redirect, render
from posts.models import Kategori, Posting
import requests
def posts_list(request):
    template_name = 'posts_list.html'
    posting_list = Posting.objects.all()
    context = {
        'title' : 'Posting List',
        'posting' : posting_list
    }
    return render(request, template_name, context)

def posts_add(request):
    template_name = 'posts_add.html'
    kategori = Kategori.objects.all()
    if request.method == "POST":
        
        input_nama = request.POST.get('nama')
        input_judul = request.POST.get('judul')
        input_body = request.POST.get('body')
        input_kategori = request.POST.get('kategori')
        input_image = request.POST.get('image')
        
        #panggil kategori 
        get_kategori = Kategori.objects.get(nama=input_kategori)
        
        #simpan posting karena ada relasi ke tabel kategori
        Posting.objects.create(
            nama = input_nama,
            judul = input_judul,
            body = input_body,
            kategori = get_kategori, 
            image = input_image,
        )
        return redirect(posts_list)
    context = {
        'title' : 'Posting Add',
        'kategori' : kategori,
    }
    return render(request, template_name, context)

def posts_update(request, id):
    template_name = 'posts_add.html'
    kategori = Kategori.objects.all()
    get_posting = Posting.objects.get(id=id)
    if request.method == "POST":
        
        input_nama = request.POST.get('nama')
        input_judul = request.POST.get('judul')
        input_body = request.POST.get('body')
        input_kategori = request.POST.get('kategori')
        input_image = request.POST.get('image')
        
        #panggil kategori 
        get_kategori = Kategori.objects.get(nama=input_kategori)
        
        #simpan posting karena ada relasi ke tabel kategori
        get_posting.nama = input_nama
        get_posting.judul = input_judul
        get_posting.body = input_body
        get_posting.kategori = get_kategori
        get_posting.image = input_image
        get_posting.save()
        
        return redirect(posts_list)
    context = {
        'title' : 'Posting Add',
        'kategori' : kategori,
        'get_posting' : get_posting,
    }
    return render(request, template_name, context)

def posts_delete(request, id):
    Posting.objects.get(id=id).delete()
    return redirect(posts_list)