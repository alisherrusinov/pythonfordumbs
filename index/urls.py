from django.urls import path, include
from compiler import views as compiler_views
from .views import index

app_name = 'index'


urlpatterns = [
    path('', index, name='index_view'),
    path('sandbox/', compiler_views.sandbox, name='sandbox')
]
