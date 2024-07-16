from django.shortcuts import render, HttpResponse, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User


def index(request):
    if request.user.is_authenticated:
        return render(request, 'index.html')
    else:
        return HttpResponse("<h1>You are not authenticated!</h1>")

def signin(request):
    name = ""
    password = ""
    if request.method == 'POST':
        name = request.POST.get("name")
        password = request.POST.get("password")
        user = authenticate(username=name, password=password)
        if user is not None:
            login(request, user)
            return redirect('home')
    return render(request, 'login.html', {'name':name,'password':password})

def signup(request):
    name = ""
    password = ""
    if request.method == 'POST':
        print("Post request recieved...")
        name = request.POST.get("name")
        password = request.POST.get("password")
        print("Name: ",name)
        print("Password: ", password)
        try:
            user = User.objects.create(username=name)
            user.set_password(password)
            user.save()
            return redirect('login')
        except Exception as e:
            print(e)
    return render(request, 'signup.html', {'name':name,'password':password})