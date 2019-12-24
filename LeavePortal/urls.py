from django.conf.urls import url
from django.contrib import admin
from . import views

urlpatterns = [
    url(r'^$', views.index),
    url('leaves/', views.leaves, name='leaves'),
]
