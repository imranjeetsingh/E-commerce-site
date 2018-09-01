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

def login_page(request):
    form = LoginForm(request.POST or None)
    context = {
        "form" : form
    }
    print(request.user.is_authenticated())
    if form.is_valid():
        print(form.cleaned_data)
        # context['form'] = LoginForm()
        username = form.cleaned_data.get('username')
        password  = form.cleaned_data.get('password')
        user     = authenticate(username=username, password=password)
        print(request.user.is_authenticated())
        if user is not None:
            print(request.user.is_authenticated())
            login(request, user)
            return redirect("/")
        else:
            print("Error")
    return render(request,"auth/login.html",context)

def register_page(request):
    form = RegisterForm(request.POST or None)
    context = {
        "form" : form
    }
    if form.is_valid():
        print(form.cleaned_data)
        username  = form.cleaned_data.get('username')
        email     = form.cleaned_data.get('email')
        password  = form.cleaned_data.get('password')
        new_user  = User.objects.create_user(username,email,password)
        print(new_user)
    return render(request,"auth/register.html",context)