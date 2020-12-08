from django.shortcuts import render
from django.views import View
# Create your views here.
from django.contrib.auth.views import LoginView, LogoutView
from django.shortcuts import render, redirect
from auth import forms
from django.contrib.auth import login


class Login(LoginView):

    template_name = 'auth/login.html'
   


class Logout(LogoutView):
    template_name = 'auth/logout.html'


class Signup(View):
    def get(self, request):
        context = {
            "form": forms.SignUpForm()
        }
        return render(request, 'auth/signup.html', context)

    def post(self, request):
        form = forms.SignUpForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect("/")
        context = {
            "form": form
        }
        return render(request, 'auth/signup.html', context)
