from django.contrib import admin
from django.urls import path, include
from mycrud.views import *
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', index, name='index'),
    path('about', about, name='about'),
    path('posts/', include('posts.urls')),
    
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
