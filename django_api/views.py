from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response

from django_api.models import Breed, Dog
from django_api.serializers import BreedSerializer, DogSerializer


@api_view(['GET', 'POST'])
def breed_list(request, format=None):
    if request.method == 'GET':
        breeds = Breed.objects.all()
        serializer = BreedSerializer(breeds, many=True)
        return Response(serializer.data)

    if request.method == 'POST':
        serializer = BreedSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)

@api_view(['GET', 'PUT', 'DELETE'])
def breed_detail(request, id, format=None):
    try:
        breed = Breed.objects.get(pk=id)
    except Breed.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = BreedSerializer(breed)
        return Response(serializer.data)

    if request.method == 'PUT':
        serializer = BreedSerializer(breed, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    if request.method == 'DELETE':
        breed.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


@api_view(['GET', 'POST'])
def dog_list(request, format=None):
    if request.method == 'GET':
        dogs = Dog.objects.all()
        serializer = DogSerializer(dogs, many=True)
        return Response(serializer.data)

    if request.method == 'POST':
        serializer = DogSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)


@api_view(['GET', 'PUT', 'DELETE'])
def dog_detail(request, id, format=None):
    try:
        dog = Dog.objects.get(pk=id)
    except Dog.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = DogSerializer(dog)
        return Response(serializer.data)

    if request.method == 'PUT':
        serializer = DogSerializer(dog, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    if request.method == 'DELETE':
        dog.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

