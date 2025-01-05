from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .models import User
from .jsonizer import UserJsonizer
from django.db import transaction
transaction.set_autocommit(True)
from django.shortcuts import get_object_or_404


@api_view(["GET"])
def get_item(request,pk):
    item = get_object_or_404(User, id=pk)
    ser = UserJsonizer(item)
    return Response(ser.data)
    

# @api_view(['GET'])
# def get_user(request, pk):
#     usr = User.objects.get(pk=pk)
#     serializer = UserJsonizer(usr)
#     return Response(serializer.data)
    
@api_view(['POST'])
def create_item(request):
    serializer = UserJsonizer(data=request.data)
    if serializer.is_valid():
        name = serializer.validated_data.get('name')
        if User.objects.filter(name=name).exists():
            return Response("Item exists",status=status.HTTP_406_NOT_ACCEPTABLE)
        else:
            serializer.save()
            return Response(serializer.data,
                            status=status.HTTP_201_CREATED)
    return Response(serializer.errors, 
                    status=status.HTTP_400_BAD_REQUEST)



# @api_view(['POST'])
# def auth(request):
#     serializer = UserJsonizer(data=request.data)
#     if serializer.is_valid():
#         username = serializer.validated_data.get('username')
#         password = serializer.validated_data.get("password")
#         try:
#             tmpuser = User.objects.get(username=username)
#             if username == tmpuser.username and password == tmpuser.password:
#                return Response("Access granted", status=status.HTTP_202_ACCEPTED)
#             else:
#                return Response(serializer.errors, status=status.HTTP_401_UNAUTHORIZED)
#         except:
#             return Response(serializer.errors, status=status.HTTP_401_UNAUTHORIZED)
#     return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)