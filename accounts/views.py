from django.shortcuts import render, redirect
from django.contrib import messages


def register(request):
    if request.method == "POST":
        #! Register Uer
        messages.error(request, "Testing Error Message")
        return redirect("register")
    else:
        return render (request, "accounts/register.html")

def login(request):
    if request.method == "POST":
        #! Login Uer
        pass
    else:
        return render (request, "accounts/login.html")


def logout(request):
    return redirect("home")

def dashboard(request):
    return render (request, "accounts/dashboard.html")