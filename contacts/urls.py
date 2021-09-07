from django.urls import path
from . import views

urlpatterns=[
    path('', views.contact, name='contacts'),
    path('contactus', views.contactus, name='contact')
]