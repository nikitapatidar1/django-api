from rest_framework.response import Response
from rest_framework.decorators import api_view
from django.db.models.functions import Lower  # Case-insensitive sorting
from .models import State, City
from .serializers import StateNameSerializer, CitySerializer


@api_view(['GET'])
def get_states(request):
    states = State.objects.all().order_by(Lower("name"))  # ✅ Alphabetically sorted states
    serializer = StateNameSerializer(states, many=True)  
    return Response(serializer.data)


@api_view(['GET'])
def get_cities(request):
    cities = City.objects.all().order_by(Lower("name"))  # ✅ Alphabetically sorted cities
    serializer = CitySerializer(cities, many=True)
    return Response(serializer.data)


@api_view(['GET'])
def get_state_cities(request, state_name):
    try:
        state = State.objects.get(name=state_name)
        cities = City.objects.filter(state=state).order_by(Lower("name"))  # ✅ Sorted cities
        serializer = CitySerializer(cities, many=True)
        return Response(serializer.data)
    except State.DoesNotExist:
        return Response({"error": "State not found"}, status=404)
