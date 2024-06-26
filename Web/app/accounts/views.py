# accounts/views.py

from django.shortcuts import render, redirect
from django.views import View
from django.contrib.auth import login, authenticate, logout
from .forms import SignUpForm, LoginForm

class SignInView(View):
    def get(self, request):
        form = SignUpForm()
        return render(request, 'Sign_in.html', {'form': form})

    def post(self, request):
        form = SignUpForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.set_password(form.cleaned_data['password'])
            user.save()
            login(request, user)
            return redirect('welcome-link')
        return render(request, 'Sign_in.html', {'form': form})

class WelcomeView(View):
    def get(self, request):
        if request.user.is_authenticated:
            if request.COOKIES.get('saw_index'):
                return redirect('home_post_creator-link')
            else:
                return redirect('home-link')
        form = LoginForm()
        return render(request, 'Welcome.html', {'form': form})

    def post(self, request):
        form = LoginForm(request, data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('home-link')
        return render(request, 'Welcome.html', {'form': form})

class LogoutView(View):
    def get(self, request):
        logout(request)
        return redirect('home-link')
