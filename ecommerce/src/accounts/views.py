from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth import authenticate, login, logout
from django.shortcuts import render, redirect
from django.utils.http import is_safe_url
# from django.conf import settings
# from django.contrib.auth.models import User
from .forms import ContactForm, LoginForm, RegisterForm, GuestForm
from .models import GuestEmail
from django.views.generic import CreateView, FormView
# Create your views here.


def guest_register_view(request):
    form = GuestForm(request.POST or None)
    context = {
        "form": form
    }
    # print(request.user.is_authenticated())
    next_ = request.GET.get('next')
    next_post = request.POST.get('next')
    redirect_path = next_ or next_post or None
    if form.is_valid():
        email            = form.cleaned_data.get('email')
        new_guest_email  = GuestEmail.objects.create(email=email)
        request.session["guest_email_id"] = new_guest_email.id
        print(new_guest_email.id)
        if is_safe_url(redirect_path, request.get_host()):
            return redirect(redirect_path)
        else:
            return redirect("/register/")
    return redirect("/register/")

class LoginView(FormView):
    form_class = LoginForm
    success_url = '/'
    template_name = 'accounts/login.html'

    def form_valid(self, form):
        request = self.request
        next_ = request.GET.get('next')
        next_post = request.POST.get('next')
        redirect_path = next_ or next_post or None
        email = form.cleaned_data.get("email")
        password = form.cleaned_data.get("password")
        user     = authenticate(username=email, password=password)
        if user is not None:
            login(request, user)
            print("heloo")
            try:
                del request.session['guest_email_id']
            except:
                pass
            if is_safe_url(redirect_path, request.get_host()):
                return redirect(redirect_path)
            else:
                return redirect("/")
        # print("error")
        return super(LoginView, self).form_invalid(form)

# def login_page(request):
#     form = LoginForm(request.POST or None)
#     context = {
#         "form": form
#     }
#     # print(request.user.is_authenticated())
#     next_ = request.GET.get('next')
#     next_post = request.POST.get('next')
#     redirect_path = next_ or next_post or None
#     if form.is_valid():
#         print(form.cleaned_data)
#         # context['form'] = LoginForm()
#         username = form.cleaned_data.get('username')
#         password = form.cleaned_data.get('password')
#         user = authenticate(username=username, password=password)
#         # print(request.user.is_authenticated())
#         if user is not None:
#             # print(request.user.is_authenticated())
#             login(request, user)
#             try:
#                 del request.session['guest_email_id']
#             except:
#                 pass
#             if is_safe_url(redirect_path, request.get_host()):
#                 return redirect(redirect_path)
#             else:
#                 return redirect("/products/")
#         else:
#             print("Error")
#     return render(request, "accounts/login.html", context)


class RegisterView(CreateView):
    form_class = RegisterForm
    template_name = "accounts/register.html"
    success_url = '/login/'

# def register_page(request):
#     form = RegisterForm(request.POST or None)
#     context = {
#         "form": form
#     }
#     if form.is_valid():
#         form.save()
#         # print(form.cleaned_data)
#         # username = form.cleaned_data.get('username')
#         # email = form.cleaned_data.get('email')
#         # password = form.cleaned_data.get('password1')
#         # new_user = User.objects.create_user(username, email, password)
#         # login(request, new_user)
#         # return redirect("/products/")
#         # print(new_user)
#     return render(request, "accounts/register.html", context)
