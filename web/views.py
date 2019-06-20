from django.shortcuts import render,redirect
import pyrebase
from django.http import Http404,HttpResponse
from django.contrib import auth

config={
  'apiKey': "AIzaSyC0Z5dua996GPaJzlwX1aK_D6FcVSxUNSo",
  'authDomain': "moveme-147d2.firebaseapp.com",
  'databaseURL': "https://moveme-147d2.firebaseio.com",
  'projectId': "moveme-147d2",
  'storageBucket': "moveme-147d2.appspot.com",
  'messagingSenderId': "183677734527",
  'appId': "1:183677734527:web:374887c94de181f5"
} 

firebase = pyrebase.initialize_app(config)
auth_d = firebase.auth()
database=firebase.database()

# Create your views here.
def welcome(request):
  return render(request, 'welcome.html')

def singIn(request):
  return render(request, "signIn.html")

def postsign(request):
  email=request.POST.get('email')
  passw = request.POST.get("pass")

  try:
    user = auth.sign_in_with_email_and_password(email,passw)

  except:
    message = "invalid cerediantials"
    return render(request,"signIn.html",{"msg":message})
  print(user['idToken'])
  session_id=user['idToken']
  request.session['uid']=str(session_id)
  return render(request, "welcome.html",{"e":email})

# driver signup
def postdriverSignup(request):
  firstname=request.POST.get('firstname')
  lastname=request.POST.get('lastname')
  email=request.POST.get('email')
  password=request.POST.get('password')
  phone=request.POST.get('mobile')

  try:
    user=auth_d.create_user_with_email_and_password(email,password)
  except:    
    message="Unable to create account! Please try again"
    return render(request,'driversignup.html',{"message":message})
  uid=user['localId']

  data={
    "firstname":firstname,
    "lastname":lastname,
    "email":email,
    "password":password,
    "mobile":phone,
   "status":"1"
  }

  database.child("Users").child(Driver).child(uid).child("details").set(data)

  return render(request,'driverlogin.html')

def driverSignup(request):
  return render(request, "driversignup.html")

# end driver signup  

# Driver signIn
def driversingIn(request):
  return render(request, "driverlogin.html")

def driverpostsignIn(request):
  email=request.POST.get('email')
  passw = request.POST.get("pass")

  try:
    user = auth_d.sign_in_with_email_and_password(email,passw)

  except:
    message = "invalid cerediantials"
    return render(request,"driverlogin.html",{"msg":message})
  print(user['idToken'])
  session_id=user['idToken']
  request.session['uid']=str(session_id)

  return render(request, "driver.html",{"e":email})
# end driver signIn



