from django.shortcuts import render,HttpResponse,redirect
from datetime import datetime
from django.utils import timezone
from home.models import Contact

def infotechhome(request):
    return render(request,'home.html')
    #return HttpResponse("this is about page")
def contact(request):
    if request.method == "POST":
        name = request.POST.get('name')
        phone = request.POST.get('phone')
        desc = request.POST.get('desc')
        email = request.POST.get('email')
        contact = Contact(name=name,email=email,desc=desc,phone=phone)
        contact.save()
    return render(request,'contact.html')
    # return HttpResponse("this is contact page")

def login(request):
    return render(request,'login.html')
def newcourse(request):
    return HttpResponse("this is new cource page")
def aboutus(request):
    return HttpResponse("this is about us  page")
