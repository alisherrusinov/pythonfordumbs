from django.shortcuts import render, reverse
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth import login, authenticate
from .forms import LoginForm
# Create your views here.


def login_view(request):
    if(request.method == 'POST'):
        form = LoginForm(request.POST)
        if(form.is_valid()):
            data = form.cleaned_data
            user = authenticate(
                request,
                username=data['username'],
                password=data['password']
            )
            if(user is not None):
                if(user.is_active):
                    login(request, user)
                    return HttpResponseRedirect(reverse('index:indexx'))
                else:
                    return HttpResponse('Disabled Account')
            else:
                return HttpResponse('invalid login')

    else:
        form = LoginForm()
        return render(request, 'registration/login.html', {'form': form})

