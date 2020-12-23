from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm, PasswordChangeForm
from django.contrib.auth import login, authenticate, update_session_auth_hash
from django.views.generic import CreateView
from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import HttpResponseRedirect


class RegisterUser(CreateView):
    form_class = UserCreationForm

    def get(self, request):
        if self.request.user.is_authenticated:
            return redirect('/')
        return render(request, 'users/register-user.html', {'form': UserCreationForm()})

    def post(self, request):
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=password)
            login(request, user)
            messages.success(request, f'Welcome, {username}!')
            return redirect('login')
        return render(request, 'users/register-user.html', {'form': form})
