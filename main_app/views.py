from django.views.generic import ListView, DetailView
from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def home(request):
    return render(request, 'home.html')

def about (request):
    return render(request, 'about.html')

def login (request):
    return render(request, 'login.html')

def logout (request):
    return render(request, 'logout.html')
