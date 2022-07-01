from django.http import HttpResponse
from django.shortcuts import render
from django.http import JsonResponse
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Task
from .serializer import TaskSerializer


# Create your views here.
@api_view(['GET'])
def ApiConfig(req):
    menu = {"/task-list/":"List all the tasks",
            "/task_detail/<str:pk>/":"Detail view of single task",
            "/create-task/":"To create(post) a new task",
            "/task-update/<str:pk>":"To update any task",
            "task-delete/<int:id>":"To delete the task",
        }
    return Response(menu)

@api_view(['GET'])
def TaskList(req):
    tasks = Task.objects.all()
    serializer = TaskSerializer(tasks,many=True) #when we serialize more than one record(object),spec.many=True
    return Response(serializer.data)

@api_view(['GET'])
def TaskDetail(req,pk):
    task = Task.objects.get(id=pk)
    serialized = TaskSerializer(task,many=False) #serialize only one object
    return Response(serialized.data)

@api_view(['POST'])
def CreateTask(req): 
    serialized = TaskSerializer(data=req.data)
    if serialized.is_valid():        
        serialized.save()
    return Response(serialized.data)

@api_view(['POST'])
def TaskUpdate(req,pk):
    task = Task.objects.get(id=pk)
    print(task)
    serializer = TaskSerializer(instance=task,data=req.data)
    if serializer.is_valid():
        serializer.save()
    print(serializer.data)
    return Response(serializer.data)

@api_view(['DELETE'])
def DeleteTask(request,id):
    task = Task.objects.get(id=id)
    task.delete()
    return Response("Task has been deleted")

