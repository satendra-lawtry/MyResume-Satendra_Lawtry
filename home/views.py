from django.shortcuts import render
from django.contrib import messages
from .models import Contacts

# Create your views here.

def home(request):
    if request.method == "POST":
        name = request.POST['name']
        email = request.POST['email']
        subject = request.POST['subject']
        message = request.POST['message']
        obj = Contacts.objects.create(name=name,email=email,subject=subject,message=message)
        obj.save()
        data = Contacts.objects.all()
        messages.success(request,"Your Contact Details Share Successfully")
        return render(request,'index.html',{'data': data,'name':name })
    return render(request,'index.html')