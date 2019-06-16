from . import views
from django.conf.urls import url,include

#urls defination to navigate through the pages
urlpatterns=[
  url(r'^dashboard/',views.dashboard,name='dashboard'),
]