from django.shortcuts import render,redirect
import pyrebase


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
auth = firebase.auth()


# Create your views here.
def welcome(request):
  return render(request, 'welcome.html')

def singIn(request):
  return render(request, "signIn.html")

def postsign(request):
  email=request.POST.get('email')
  passw = request.POST.get("pass")

  # try:
  #   user = auth.sign_in_with_email_and_password(email,passw)

  # except:
  #   message = "invalid cerediantials"

  # return render(request,"signIn.html",{"msg":message})
  # print(user)
  return render(request, "welcome.html",{"e":email})
