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
