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

def trips(request):

  return render(request,'trips.html')

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
  
  return render(request, "welcome.html",{"email":email,"user":user})

def adminLogout(request):
  try:
    del request.session['uid']
  except KeyError:
    pass

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
  url =request.POST.get('url')
  bio=request.POST.get('bio')
  try:
    time_now=datetime.now()
    millis=int(time.mktime(time_now.timetuple()))
    idToken=request.session['uid']
    prof =auth_a.get_account_info(idToken)

    prof=prof['users']
    prof=prof[0]
    prof=prof['localId']

    print("Prof"+str(prof))   

    data={
      'name':name,
      'address':address,
      'mobile':mobile,
      'url':url,
      'bio':bio
    }
    database.child("admin").child(prof).child("profile").child(millis).set(data,idToken)

    return render(request,'dashboard.html')
  except KeyError:
    message='Oops! User logged out please sign in.'
    return render(request,'signIn.html',{"message":message})

def adminDetails(request):
  idToken=request.session['uid']
  # print(idToken)
  prof =auth_a.get_account_info(idToken)
  # print(prof)
  current_user = prof['users']
  current_user_id = current_user[0]
  now_user = current_user_id['localId']

  # print(now_user)

  prof=prof['users']
  prof=prof[0]
  prof=prof['localId']
  db = firebase.database()
  admins = db.child("admin").child(now_user).child('profile').get().val()
  # print(admins)

  lis_time=[]

  for profile in admins:
    lis_time.append(profile)

    lis_time.sort(reverse=True)

  recent_profile = lis_time[-1]
  print(recent_profile)
  recent_profile_details = admins[recent_profile]
  recent_address = recent_profile_details['address']
  rec_contact = recent_profile_details['mobile']
  name = recent_profile_details['name']
  print(recent_address)
    
  return render(request,'administrator.html',{'address':recent_address,'contact':rec_contact,'name':name})

def location(request):
  
  return render(request,'location_rates.html')