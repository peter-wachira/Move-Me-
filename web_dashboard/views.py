from django.shortcuts import render,redirect
from django.http import Http404,HttpResponse
import pyrebase
from django.contrib import auth
import time
from datetime import datetime

config={
  'apiKey': "AIzaSyC0Z5dua996GPaJzlwX1aK_D6FcVSxUNSo",
  'authDomain': "moveme-147d2.firebaseapp.com",
  'databaseURL': "https://moveme-147d2.firebaseio.com",
  'projectId': "moveme-147d2",
  'storageBucket': "moveme-147d2.appspot.com",
  'messagingSenderId': "183677734527",
  'appId': "1:183677734527:web:3d6d59226b572354"
}

firebase = pyrebase.initialize_app(config)
auth_a = firebase.auth()
database=firebase.database()

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

def postsign(request):
  email = request.POST.get('email')
  password = request.POST.get('pass')

  try:
    user = auth_a.sign_in_with_email_and_password(email,password)
  except:
    message = "Invalid Credentials"
    return render(request,"signIn.html",{"message":message})
  print(user['idToken'])
  session_id=user['idToken']
  request.session['uid']=str(session_id)
  
  return render(request, "welcome.html",{"email":email})

def adminLogout(request):
  auth.logout(request)

  return render(request,'signIn.html')

def adminRegister(request):

  return render(request,'signUp.html')

def postsignup(request):
  firstname=request.POST.get('firstname')
  lastname=request.POST.get('lastname')
  email=request.POST.get('email')
  password=request.POST.get('password')
  phone=request.POST.get('mobile')

  try:
    user=auth_a.create_user_with_email_and_password(email,password)
  except:    
    message="Unable to create account! Please try again"
    return render(request,'signUp.html',{"message":message})
  uid=user['localId']

  data={
    "firstname":firstname,
    "lastname":lastname,
    "email":email,
    "password":password,
    "phone":phone,
  }

  database.child("admin").child(uid).child("details").set(data)

  return render(request,'signIn.html')

def create_profile(request):

  return render(request,'welcome.html')

def post_create(request):
  name=request.POST.get('name')
  address=request.POST.get('address')
  mobile=request.POST.get('phone')
  bio=request.POST.get('bio')

  time_now=datetime.now()
  milis=int(time.mktime(time_now.timetuple()))
  idToken=request.session['uid']
  prof =auth_a.get_account_info(idToken)

  print("Prof"+str(prof))   

  data={
    'name':name,
    'address':address,
    'mobile':mobile,
    'bio':bio
  }

  return render(request,'dashboard.html')

