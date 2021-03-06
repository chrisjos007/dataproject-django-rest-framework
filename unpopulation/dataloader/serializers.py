from rest_framework import serializers
from .models import PopulationData


class FirstSerializer(serializers.ModelSerializer):
    class Meta:
        model = PopulationData
        fields = ['country', 'year', 'population']


class SecondSerializer(serializers.Serializer):
    year = serializers.IntegerField()
    total_population = serializers.FloatField()

    class Meta:
        ordering = ['year']
