from django.urls import path, include
from .views import index, editor

urlpatterns = [
    path('', index),
    path('editor', editor, name='editor')
]