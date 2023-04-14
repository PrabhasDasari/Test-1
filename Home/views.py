from django.shortcuts import render, HttpResponse
from .models import Contact

def home_page(request):
    return render(request,'Home/index.html')
def login_page(request):
    return render(request,'Home/login.html')
def contact(request):
    if request.method=="POST":
        name = request.POST.get('name', '')
        email = request.POST.get('email', '')
        phone = request.POST.get('phone', '')
        desc = request.POST.get('desc', '')
        contact = Contact(name=name, email=email, phone=phone, desc=desc)
        contact.save()
        return HttpResponse("<h1>Response recorded successfully!</h1><br><a style='color: green;' href='/home'>return to home</a>")
    return render(request, 'Home/contact.html')
