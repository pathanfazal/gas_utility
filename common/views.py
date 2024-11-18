# common/views.py
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login as auth_login
from django.contrib.auth.forms import AuthenticationForm
from django.contrib import messages
from django.contrib.auth.forms import UserCreationForm 


def home(request):
    return render(request, 'common/home.html')

# common/views.py
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login as auth_login
from django.contrib.auth.forms import AuthenticationForm
from django.contrib import messages
from django.contrib.auth.forms import UserCreationForm 


def home(request):
    return render(request, 'common/home.html')

def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Registration successful!')
            return redirect('common:login')  # Redirect to login page after successful registration
        else:
            form = UserCreationForm()
    
    return render(request, 'common/register.html', {'form': form})
def login(request):
    if request.method == "POST":
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            # Authenticate user
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(request, username=username, password=password)

            if user is not None:
                # Log in the user
                auth_login(request, user)
                return redirect('customer:dashboard')  # Redirect to the dashboard
            else:
                messages.error(request, "Invalid credentials, please try again.")
        else:
            messages.error(request, "Invalid credentials, please try again.")
    else:
        form = AuthenticationForm()

    return render(request, 'common/login.html', {'form': form})

def login(request):
    if request.method == "POST":
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            # Authenticate user
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(request, username=username, password=password)

            if user is not None:
                # Log in the user
                auth_login(request, user)
                return redirect('customer:dashboard')  # Redirect to the dashboard
            else:
                messages.error(request, "Invalid credentials, please try again.")
        else:
            messages.error(request, "Invalid credentials, please try again.")
    else:
        form = AuthenticationForm()

    return render(request, 'common/login.html', {'form': form})
