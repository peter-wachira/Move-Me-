from django.shortcuts import render,redirect
from django.http import Http404,HttpResponse

# Create your views here.
def dashboard(request):

  return render(request,'dashboard.html')

def admin(request):

  return render(request,'administrator.html')

def users(request):

  return render(request,'users.html')

def drivers(request):

  return render(request,'drivers.html')