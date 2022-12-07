from django.contrib import admin
from posts.models import *

# Register your models here.
admin.site.register(Kategori)
class PostingAdmin(admin.ModelAdmin):
    list_display = ['nama', 'judul', 'body', 'kategori', 'image']
admin.site.register(Posting, PostingAdmin)

