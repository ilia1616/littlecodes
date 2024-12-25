from django.urls import path
from .views import get_user, create_user

urlpatterns =[path('user/<str:name>', get_user ,name='get_user'),
              path('create/', create_user,name='create_user')]
# this file most have urlpatterns
# if not the server wont run
