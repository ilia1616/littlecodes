from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .models import User
from .jsonizer import UseSerializer

@api_view(['GET'])
def get_user(request):
    return Response(UseSerializer({'username':'yaghob','password':'yaghob'}))