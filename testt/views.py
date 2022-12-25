from django.shortcuts import render,redirect
from django.views import View
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth import logout,login,authenticate
from django.http import HttpResponseRedirect
from django import forms

class LoginForm(forms.Form):
    username = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput())
class Front(View):
    def get(self,request):
        return render(request,"testt/index.html",{"form":LoginForm})

class Backend(LoginRequiredMixin,View):
    def get(self,request):
        return render(request,"testt/backend.html")

class Login(View):
    def post(self,request):
        form = LoginForm(request.POST)
        if form.is_valid():
            user = authenticate(username=form.cleaned_data["username"],password=form.cleaned_data["password"])
            if user:
                login(request,user)
                return redirect("backend")
        return render(request,"testt/index.html",{"form":form})

class Logout(View):
    def get(self,request):
        logout(request)
        return HttpResponseRedirect("/")

# Create your views here.
