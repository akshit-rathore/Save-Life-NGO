from django.db import models
from django.shortcuts import redirect, render
from django.contrib.auth import logout
from django.contrib.auth.models import User
from django.contrib import messages, auth
from django.contrib.auth.decorators import login_required
from donations.models import donation
from .import my_id

# Create your views here.

def login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        user = auth.authenticate(username=username, password=password)

        if user is not None:
            auth.login(request, user)
            my_id.id = username
            return redirect('dashboard')
        else:
            messages.warning(request, "Invalid Credentials")
            return redirect('login')

    return render(request, 'webpages/login.html')

def register(request):
    if request.method == 'POST':
        name = request.POST['name']
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']

        if User.objects.filter(username=username).exists():
            messages.warning(request, "Username exists")
            return redirect('register')
        else:
            if User.objects.filter(email=email).exists():
                messages.warning(request, "Email exists")
                return redirect('register')
            else:   
                user = User.objects.create_user(first_name=name, username=username, email=email, password=password)
                user.save()
                messages.success(request, "Account created")
                return redirect('login')

    return render(request, 'webpages/register.html')

    

def logout_user(request):
    logout(request)
    return redirect('home')

@login_required(login_url='login')
def dashboard(request):
    bills = donation.objects.filter(username=my_id.id, order_status=1)
    data = {
        'bills': bills,
    }
    return render(request, 'webpages/dashboard.html', data)