from django.urls import path
from .views import get_user, create_user, auth

urlpatterns =[path('user/<int:pk>', get_user ,name='get_user'),
              path('create/', create_user,name='create_user'),
              path('auth/', auth, name="authentication")
              ]
# this file most have urlpatterns
# if not the server wont run
