from django.conf.urls import url
from . import views

urlpatterns=[
    url('^$',views.welcome,name = 'welcome'),
    url(r'^signin/$',views.singIn,name = 'web'),
    url(r'^postsign/',views.postsign,name = 'postsign'),
]