from rest_framework import serializers
from .models import User

class UserJsonizer(serializers.ModelSerializer):
    class Meta:
        model = User # what to serialize(jsonize)
        fields = '__all__' # which fiels should i serialize?