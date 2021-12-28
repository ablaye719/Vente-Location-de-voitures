from rest_framework import serializers
from .models import Car


class CarSerializer(serializers.ModelSerializer):
    """Serializer for the car object"""

    date = serializers.DateField(format="%d-%m-%Y")

    class Meta:
        model = Car
        fields = ('name', 'marque', 'date', 'price', 'kilometrage', 'image')

    def create(self, validated_data):
        """Create a new car"""
        return Car.objects.create(**validated_data)

    def update(self, instance, validated_data):
        car = super().update(instance, validated_data)
        car.save()
        return car



