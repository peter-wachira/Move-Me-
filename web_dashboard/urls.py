from . import views
from django.conf.urls import url,include

#urls defination to navigate through the pages
urlpatterns=[
  url(r'^dashboard/',views.dashboard,name='dashboard'),
  url(r'^administrator/',views.admin,name='admin-dash'),
  url(r'^users/',views.users,name='users'),
  url(r'^drivers/',views.drivers,name='drivers'),
  url(r'^signIn/',views.adminSignIn,name='admin-signIn'),
  url(r'^postsign/',views.postsign,name='admin-welcome'),
  url(r'^logout/',views.adminLogout,name='logout')
]