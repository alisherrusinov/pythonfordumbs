from django.urls import path, include
from compiler import views as compiler_views
from .views import index, lesson_detail

app_name = 'course'

urlpatterns = [
    path('', index, name='index'),
    path('<slug:lesson_slug>', lesson_detail, name='lesson_detail'),
    path('<slug:lesson_slug>/homework', compiler_views.homework, name='homework_check')
]