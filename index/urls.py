from django.urls import path, include
from .views import index

app_name = 'index'


urlpatterns = [
    path('', index, name='index_view'),
]
