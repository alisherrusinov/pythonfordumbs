from django.shortcuts import render, reverse
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth import login, authenticate
from django.contrib.auth.decorators import login_required
from .forms import LoginForm, RegistrationForm
# Create your views here.

def registration(request):
    if(request.method == 'POST'):
        form = RegistrationForm(request.POST)
        if(form.is_valid()):
            user = form.save(commit=False)
            user.set_password(form.cleaned_data['password'])
            user.save()
            return render(
                request,
                'accounts/register_done.html',
                {'new_user': user}
            )
    else:
        form = RegistrationForm()
    return render(request, 'accounts/register.html', {'form': form})


@login_required
def profile_view(request):
    # TODO: инфа о пользователе: школа, учитель, прогресс по курсу.
    return render(request, 'accounts/profile.html')

