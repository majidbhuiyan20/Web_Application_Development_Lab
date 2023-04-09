from rest_framework import serializers

from django_api.models import Breed, Dog


class BreedSerializer(serializers.ModelSerializer):
    class Meta:
        model = Breed
        fields = ('id', 'name', 'size', 'friendliness', 'trainability', 'shedding_amount', 'excercise_needs')


class DogSerializer(serializers.ModelSerializer):
    breed = serializers.SlugRelatedField(slug_field='name', queryset=Breed.objects.all())
    class Meta:
        model = Dog
        fields = ('id', 'name', 'age', 'gender', 'color', 'favourite_food', 'favourite_toy', 'breed')