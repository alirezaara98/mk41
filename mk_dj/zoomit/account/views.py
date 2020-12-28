from django.contrib.auth import authenticate, login, logout
from django.shortcuts import render, redirect
from django.contrib.auth.views import LoginView, LogoutView
from django.views.generic.edit import BaseFormView
from .forms import user_reg_form
from .models import User


# Create your views here.

class UserLogin(LoginView):
    def post(self, request, *args, **kwargs):
        username = request.POST.get('username', None)
        password = request.POST.get('password', None)
        user = authenticate(request, username=username, password=password)
        if user and user.is_active:
            login(request, user)
            return redirect('post_archive')
        return render(request, 'registration/login.html', context={})


# def user_login(request):
#     if request.method == 'POST':
#         username = request.POST.get('username', None)
#         password = request.POST.get('password', None)
#         user = authenticate(request, username=username, password=password)
#         if user and user.is_active:
#             login(request, user)
#             return redirect('post_archive')
#         else:
#             pass
#     return render(request, 'blog/login.html', context={})

class UserRegister(BaseFormView):
    def post(self, request, *args, **kwargs):
        form = user_reg_form(request.POST)
        if form.is_valid():
            # username = form.cleaned_data['username']
            password = form.cleaned_data['password1']
            full_name = form.cleaned_data['full_name']
            email = form.cleaned_data['mail']
            User.objects.create_user(email=email, full_name=full_name, password=password)
            return redirect('login')
        context = {'form': form}
        return render(request, 'registration/register.html', context)

    def get(self, request, *args, **kwargs):
        form = user_reg_form()
        context = {'form': form}
        return render(request, 'registration/register.html', context)


# def user_register(request):
#     if request.method == 'POST':
#         form = user_reg_form(request.POST)
#         if form.is_valid():
#             # username = form.cleaned_data['username']
#             password = form.cleaned_data['password1']
#             full_name = form.cleaned_data['full_name']
#             email = form.cleaned_data['mail']
#             User.objects.create_user(email=email, full_name=full_name, password=password)
#             return redirect('login')
#         else:
#             pass
#         context = {'form': form}
#     else:
#         form = user_reg_form()
#         context = {'form': form}
#     return render(request, 'registration/register.html', context)

class UserLogout(LogoutView):
    def get(self, request, *args, **kwargs):
        logout(request)
        return redirect('main_page')
# def user_logout(request):
#     logout(request)
#     return redirect('main_page')
