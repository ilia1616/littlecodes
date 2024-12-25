from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .models import User
from .jsonizer import UserJsonizer

@api_view(['GET'])
def get_user(request):
    return Response(UserJsonizer({'username':'admin',
                                  'password':'admin'}).data)
    
@api_view(['POST'])
def create_user(request):
    serializer = UserJsonizer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data,
                        status=status.HTTP_201_CREATED)
    return Response(serializer.errors, 
                    status=status.HTTP_400_BAD_REQUEST)