from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .models import User
from .jsonizer import UserJsonizer

@api_view(['GET'])
def get_user(request, pk):
    usr = User.objects.get(pk=pk)
    serializer = UserJsonizer(usr)
    return Response(serializer.data)
    
@api_view(['POST'])
def create_user(request):
    serializer = UserJsonizer(data=request.data)
    if serializer.is_valid():
        username = serializer.validated_data.get('username')
        password = serializer.validated_data.get('password')
        new_user = User.objects.create(username=username, password=password)
        return Response(new_user,
                        status=status.HTTP_201_CREATED)
    return Response(serializer.errors, 
                    status=status.HTTP_400_BAD_REQUEST)



@api_view(['POST'])
def auth(request):
    serializer = UserJsonizer(data=request.data)
    if serializer.is_valid():
        username = serializer.validated_data.get('username')
        password = serializer.validated_data.get("password")
        if username == 'admin' and password == 'admin':
            return Response("Access granted", status=status.HTTP_202_ACCEPTED)
        else:
            return Response(serializer.errors, status=status.HTTP_401_UNAUTHORIZED)
    return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)