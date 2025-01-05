from django.urls import path
from .views import get_item, create_item

urlpatterns =[
              path('getitem/<int:pk>', get_item, name='get_item'),
            #   path('user/<int:pk>', get_user ,name='get_user'),
              path('create/', create_item, name='create_user'),
            #   path('auth/', auth, name="authentication"),
              ]
# this file most have urlpatterns
# if not the server wont run
