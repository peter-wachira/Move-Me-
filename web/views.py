from django.shortcuts import render
import pyrebase


config = {
  apiKey: "AIzaSyC0Z5dua996GPaJzlwX1aK_D6FcVSxUNSo",
  authDomain: "moveme-147d2.firebaseapp.com",
  databaseURL: "https://moveme-147d2.firebaseio.com",
  projectId: "moveme-147d2",
  storageBucket: "moveme-147d2.appspot.com",
  messagingSenderId: "183677734527",
  appId: "1:183677734527:web:374887c94de181f5"
} 

firebase = pyrebase.initialize_app(config)
auth = firebase.auth()


# Create your views here.
def welcome(request):
    return render(request, 'welcome.html')

def singIn(request):
return render(request, "signIn.html")