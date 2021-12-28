from rest_framework import generics

from .Serializers import CarSerializer
from .models import Car


class ListCarView(generics.ListAPIView):
    """List all cars"""
    serializer_class = CarSerializer
    queryset = Car.objects.all()


class CreateCarVew(generics.CreateAPIView):
    """Create a new car"""
    serializer_class = CarSerializer


class ManageCarView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Car.objects.all()
    serializer_class = CarSerializer
