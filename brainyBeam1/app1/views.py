from django.http import HttpResponse
from django.shortcuts import render,redirect
from .forms import RegistrationForm
from django.contrib import messages
from .models import User

def base(request):
    return render(request, 'base.html')
    #'''return HttpResponse("Welcome to app1!")'''

def login_view(request):
    return render(request, 'login.html')

def register(request):
    return render(request, 'register.html')

def registration(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        reenter_password = request.POST['reenter_password']

        if password != reenter_password:
            messages.error(request, "Passwords do not match.")
            return render(request, 'register.html')

        if User.objects.filter(username=username).exists():
            messages.error(request, "Username is already taken.")
            return render(request, 'register.html')

        user = User(username=username, password=password)
        user.save()
        messages.success(request, "Registration successful.")
        return redirect('login')  # Redirect to the login page or another page

    return render(request, 'base.html')



def logging(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        try:
            user = User.objects.get(username=username)
            if user.password == int(password):
                return render(request, 'home.html')  # Redirect to the home page
            else:
                messages.error(request, "Invalid password.")
                return render(request, 'login.html')
        except User.DoesNotExist:
            messages.error(request, "Username does not exist.")
            return render(request, 'login.html')

    return render(request, 'login.html')
