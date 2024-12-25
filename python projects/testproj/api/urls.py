from django.urls import path
from .views import get_user

urlpattern =[path('user/',get_user,name='get_user')]