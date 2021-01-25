from django.shortcuts import render, redirect

def register(request):
    if request.method == "POST":
        #! Register Uer
        pass
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