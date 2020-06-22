from django.shortcuts import render, redirect
from .forms import *


def signup(request):
    if request.method == 'POST':
        form = SignupForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('signin')
        else:
            return redirect('errorpage')
    else:
        form = SignupForm()
        return render(request, 'signup.html', {'form': form})


def signin(request):
    form = SigninForm()
    return render(request, 'signin.html', {'form': form})
