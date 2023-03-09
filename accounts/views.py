from django.urls import reverse
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.contrib.auth import logout
from django.core.paginator import Paginator
from .forms import SignupForm
from django.contrib import messages



def signup(request):
    if request.method == "POST":
        form = SignupForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data['username']
            password = form.cleaned_data['password1']
            user = authenticate(username=username, password=password)
            messages.success(request, "Registration sucessful")
            login(request, user)
            return redirect('home:home_render')
        else:
            messages.error(request, form.errors)
            return redirect('accounts:signup')
    else:
        form = SignupForm()
    return render(request, 'registration/signup.html', {'form': form})

   


def logout_view(request):
    logout(request)
