from rest_framework import serializers
from .models import State, City

class StateNameSerializer(serializers.ModelSerializer):
    class Meta:
        model = State
        fields = ['name'] 

class CitySerializer(serializers.ModelSerializer):
    state = serializers.CharField(source='state.name')  # State ko direct naam me convert karo

    class Meta:
        model = City
        fields = ['id', 'name', 'state']