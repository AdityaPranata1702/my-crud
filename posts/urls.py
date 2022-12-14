from django.urls import path
from posts.views import *

urlpatterns = [
    path('', posts, name='posts'),
    path('list/', posts_list, name='posts_list'),
    path('add/', posts_add, name='posts_add'),
    path('update/<int:id>', posts_update, name='posts_update'),
    path('delete/<int:id>', posts_delete, name='posts_delete')
    
]
