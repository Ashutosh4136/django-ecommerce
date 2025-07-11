# accounts/views.py
from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login
from django.http import HttpResponseRedirect

def signup_view(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)  # Automatically log in after registration
            return redirect('/')  # Redirect to home
    else:
        form = UserCreationForm()
    return render(request, 'accounts/singup.html', {'form': form})
def logout(request):
    logout(request)
    return redirect('logout')