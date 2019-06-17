from django.shortcuts import render,redirect
from django.http import Http404,HttpResponse
import pyrebase

config={
  apiKey: "AIzaSyC0Z5dua996GPaJzlwX1aK_D6FcVSxUNSo",
  authDomain: "moveme-147d2.firebaseapp.com",
  databaseURL: "https://moveme-147d2.firebaseio.com",
  projectId: "moveme-147d2",
  storageBucket: "moveme-147d2.appspot.com",
  messagingSenderId: "183677734527",
  appId: "1:183677734527:web:3d6d59226b572354"
}

firebase = pyrebase.initialize_app(config)
auth = firebase.auth()

# Create your views here.
def dashboard(request):

  return render(request,'dashboard.html')

def admin(request):

  return render(request,'administrator.html')

def users(request):

  return render(request,'users.html')

def drivers(request):

  return render(request,'drivers.html')

def adminSignIn(request):
  
  return render(request,'signIn.html')