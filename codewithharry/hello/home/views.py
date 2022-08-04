from django.shortcuts import render, HttpResponse
from datetime import datetime
from home.models import Contact
from django.contrib import messages

# Create your views here.


def index(request):
    context = {
        'variable':"This is sent",
        'v2': "This is variable2"
    }
    return render(request, 'index.html',context)
    # return HttpResponse("This is Home Page")

def about(request):
    # return HttpResponse("This is About Page")
    return render(request, 'about.html')

def services(request):
    # return HttpResponse("This is services Page")
    return render(request, 'services.html')

def contact(request):
    # return HttpResponse("This is contact Page")
    if request.method == "POST":
        name = request.POST.get('fname')
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        des = request.POST.get('des')
        contact = Contact(name=name,email=email,phone=phone,des=des,date=datetime.today())
        contact.save()
        messages.success(request, 'Your Message Has Been Sent.')

    return render(request, 'contact.html')
