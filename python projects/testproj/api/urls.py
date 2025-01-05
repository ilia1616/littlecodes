from django.urls import path
from .views import get_user, create_item, auth, get_item

urlpatterns =[path('user/<int:pk>', get_user ,name='get_user'),
              path('create/', create_item,name='create_user'),
              path('auth/', auth, name="authentication"),
              path('getitem/<int:pk>', get_item, name='get_item')
              ]
# this file most have urlpatterns
# if not the server wont run
