from django.urls import path
from .views import get_states, get_cities, get_state_cities

urlpatterns = [
    path('states/', get_states, name='states'),
    path('cities/', get_cities, name='cities'),
    path('states/<str:state_name>/cities/', get_state_cities, name='state-cities'),
]
