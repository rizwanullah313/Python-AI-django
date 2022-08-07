from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import logout, authenticate, login

# password for test user is Harry$$$***000
# Create your views here.
def index(request):
    print(request.user)
    if request.user.is_anonymous:
        return redirect("/login") 
    return render(request, 'index.html')

def loginUser(request):
    if request.method=="POST":
        useremail = request.POST.get('useremail')
        password = request.POST.get('password')
        print(useremail, password)

        # check if user has entered correct credentials
        user = authenticate(useremail=useremail, password=password)
        print("hello user ",user)
        if request.user is not None:
            # A backend authenticated the credentials
            login(request, user)
            print("hello abc")
            return redirect("/")

        else:
            # No backend authenticated the credentials
            return render(request, 'login.html')

    return render(request, 'login.html')

def logoutUser(request):
    logout(request)
    return redirect("/login")