from django.urls import path, include
from .views import login_view
from django.contrib.auth import views as auth_views

app_name = 'accounts'


urlpatterns = [
    path('', login_view),
    path('login/', auth_views.LoginView.as_view(), name='log-in'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
]
