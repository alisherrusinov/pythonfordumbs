from django.shortcuts import render, reverse
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth import login, authenticate
from django.contrib.auth.decorators import login_required
from .forms import LoginForm
# Create your views here.


@login_required
def profile_view(request):
    # TODO: инфа о пользователе: школа, учитель, прогресс по курсу.
    return render(request, 'accounts/profile.html')
