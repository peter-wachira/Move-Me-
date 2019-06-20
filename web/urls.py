from django.conf.urls import url
from . import views

urlpatterns=[
    url('^$',views.welcome,name = 'welcome'),
    url(r'^signin/$',views.singIn,name = 'web'),
    url(r'^postsign/',views.postsign,name = 'postsign'),
    url(r'^driverRegister/',views.driverSignup,name ='signup'),
    url(r'^postdriverSignup/',views.postdriverSignup,name = 'postdriverSignup'),
    url(r'^driverSignin/',views.driversingIn,name ='signIn'),
    url(r'^driverpostsignIn/',views.driverpostsignIn,name = 'driverpostsignIn'),
    
]
