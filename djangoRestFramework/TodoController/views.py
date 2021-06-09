from django.http import JsonResponse
from django.shortcuts import render
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Todo
from .serializers import TodoSerializer
# Create your views here.


@api_view(['GET'])
def ApiOverview(request):
	api_urls = {
		'List':'/getall/',
		'Detail View':'/get/<str:pk>/',
		'Create':'/<str:pk>/',
		'Update':'/put/<str:pk>/',
		'Delete':'/delete/<str:pk>/',
		}

	return Response(api_urls)


@api_view(['POST'])
def TodoCreate(request, pk):
    todo = Todo.objects.create(id=pk)
    serializer = TodoSerializer( instance=todo, data=request.data)
    if serializer.is_valid():
        serializer.save()
        return JsonResponse(serializer.data, status=201)
    return JsonResponse(serializer.errors, status=400)


@api_view(['GET'])
def TodoList(request):
	todo = Todo.objects.all().order_by('-id')
	serializer = TodoSerializer(todo, many=True)
	return Response(serializer.data)


@api_view(['GET'])
def TodoDetail(request, pk):
	todo = Todo.objects.get(id=pk)
	serializer = TodoSerializer(todo, many=False)
	return Response(serializer.data)


@api_view(['POST'])
def TodoUpdate(request, pk):
    todo = Todo.objects.get(id=pk)
    serializer = TodoSerializer(instance=todo, data=request.data)
    if serializer.is_valid():
        serializer.save()
        return JsonResponse(serializer.data, status=201)
    return JsonResponse(serializer.errors, status=400)



@api_view(['DELETE'])
def TodoDelete(request, pk):
	todo = Todo.objects.get(id=pk)
	todo.delete()
	serializer = TodoSerializer()
	# return Response(serializer.)
	return Response('Item succsesfully delete!')



