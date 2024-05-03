from django.shortcuts import render
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import TaskSerializer
from .models import Task

# Create your views here.

@api_view(['GET'])
def allAPIView(request):
    api_urls = {
        'List' : '/task-list/',
        'Detail View': '/task-detail/<str:pk>/',
        'Create': '/add-task/',
        'Update': '/update-task/<str:pk>/',
        'Delete' : '/delete-task/<str:pk>/',
    }
    return Response(api_urls)

@api_view(['GET'])
def taskList(request):
    tasks = Task.objects.all().order_by('-id')
    serializer = TaskSerializer(tasks, many=True)
    return Response(serializer.data)


@api_view(['GET'])
def taskDetail(request, pk):
    tasks = Task.objects.get(id=pk)
    serializer = TaskSerializer(tasks, many=False)
    return Response(serializer.data)


@api_view(['POST'])
def addTask(request):
    serializer = TaskSerializer(data = request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=201)  # Return success response with serialized data
    return Response(serializer.errors, status=400)  # Return error response with serializer errors



@api_view(['POST'])
def updateTask(request, pk):
    try:
        task = Task.objects.get(id=pk)
    except Task.DoesNotExist:
        return Response({"error": "Task not found"}, status=status.HTTP_404_NOT_FOUND)
    
    serializer = TaskSerializer(instance = task, data = request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=200) # Return 200 upon successful update
    return Response(serializer.errors, status=400) # Return 400 if there are validation errors


@api_view(['DELETE'])
def deleteTask(request, pk):
    try:
        task = Task.objects.get(id=pk)
    except Task.DoesNotExist:
        return Response({"error": "Task not found"}, status=status.HTTP_404_NOT_FOUND)
    
    task.delete()
    return Response(status=status.HTTP_204_NO_CONTENT)
   


