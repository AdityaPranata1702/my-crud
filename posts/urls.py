from django.urls import path
from posts.views import *
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('list/', posts_list, name='posts_list'),
    path('add/', posts_add, name='posts_add'),
    path('update/<int:id>', posts_update, name='posts_update'),
    path('delete/<int:id>', posts_delete, name='posts_delete')
    
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
