from django.shortcuts import render
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import TaskSerializer
from .models import Task
from django.template.loader import render_to_string
from django.core.mail import EmailMultiAlternatives

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
    sort_by =  request.query_params.get('sort_by')
  
    tasks = Task.objects.filter(user=request.user)
    tasks = tasks.order_by('-id')
    
    if sort_by == 'priority-des':
        tasks = tasks.order_by('-priority')

    elif sort_by == 'priority-asc':
        tasks = tasks.order_by('priority') 

    elif sort_by == 'due_date-asc':
        tasks = tasks.order_by('due_date') 

    elif sort_by == 'due_date-des':
        tasks = tasks.order_by('-due_date') 

    elif sort_by == 'todo':
        tasks = Task.objects.filter(completed=False, user=request.user)

    elif sort_by == 'completed':
        tasks = Task.objects.filter(completed=True, user=request.user)

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
        user = serializer.save()
        email_subject = "Task Added"
        email_body = render_to_string('taskAdded_mail.html', {'task': user})
        email = EmailMultiAlternatives(email_subject, '', to=[user.user.email])
        email.attach_alternative(email_body, "text/html")
        email.send()
        print(user)
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
        user = serializer.save()
        if user.completed:
            email_subject = "Task Completed"
            email_body = render_to_string('taskCompleted_mail.html', {'task': user})
            email = EmailMultiAlternatives(email_subject, '', to=[user.user.email])
            email.attach_alternative(email_body, "text/html")
            email.send() 
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
   


