from django.urls import path, include
from .views import profile_view, registration
from django.contrib.auth import views as auth_views

app_name = 'accounts'


urlpatterns = [
    path('login/', auth_views.LoginView.as_view(), name='log-in'),
    path('logout/', auth_views.LogoutView.as_view(
        next_page=None,
        template_name='registration/logged_out.html',),
         name='logout'),
    path('profile/', profile_view, name='profile'),
    path('register/', registration, name='register')
]
