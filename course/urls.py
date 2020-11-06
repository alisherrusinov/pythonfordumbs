from django.urls import path, include
from .views import index, lesson_detail
urlpatterns = [
    path('', index, name='index'),
    path('<slug:lesson_slug>', lesson_detail, name='lesson_detail')
]
