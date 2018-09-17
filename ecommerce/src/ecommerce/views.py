from django.http import HttpResponse
from django.contrib.auth import authenticate, login,get_user_model, logout
from django.shortcuts import render, redirect
from .forms import ContactForm, LoginForm, RegisterForm

User = get_user_model()

def home_page(request):
    context = {
        "title" : 'Home Page',
        "content" : "Welcome to Home page"
    }
    if request.user.is_authenticated():
        context["premium"] = "Yeahhhh"
    return render(request,"index.html",context)

def about_page(request):
    context = {
        "title" : 'About Page',
        "content" : "Welcome to About page"
    }
    return render(request,"index.html",context)

def contact_page(request):
    form    = ContactForm(request.POST or None)
    context = {
        "title" : 'Contact Page',
        "content" : "Welcome to Contact page",
        "form"     : form,
        "brand"     :"New Brand Name"
    }
    if form.is_valid():
        print(form.cleaned_data)
    # if request.method == "POST":
    #     print(request.POST.get('fullname'))
    #     print(request.POST.get('email'))
    #     print(request.POST.get('content'))
    return render(request,"contact/contact.html",context)
