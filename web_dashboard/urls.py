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
  url(r'^logout/',views.adminLogout,name='logout'),
  url(r'^signUp/',views.adminRegister,name='admin-signUp'),
  url(r'^postsignup/',views.postsignup,name='admin-register'),
  url(r'^profile/',views.create_profile,name='prof-create'),
  url(r'^create_post/',views.post_create,name='prof-post'),
  url(r'^user_details/',views.user_details,name='user_details')
]