from django.contrib.auth import logout
from django.contrib.auth.views import LoginView
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse

from users.forms import RegisterUserForm


class CustomLoginView(LoginView):
    template_name = 'users/login.html'
    extra_context = {'section_name': 'login'}


def logout_user(request):
    logout(request)
    return HttpResponseRedirect(reverse('home:start'))


def register_user(request):
    if request.method == 'POST':
        form = RegisterUserForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.set_password(form.cleaned_data['password'])
            user.save()
            return render(request, 'users/register_done.html', {'section_name': 'register done'})
    else:
        form = RegisterUserForm()
    return render(request, 'users/register.html', {'form': form, 'section_name': 'register'})
