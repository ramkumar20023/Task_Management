from django.shortcuts import render
from .models import User,Task
from .serializer import UserSerializer,TaskSerializer
from rest_framework .views import APIView
from rest_framework .response import Response
from rest_framework import status as rest_status
from rest_framework import status
from django .shortcuts import get_object_or_404
# Create your views here.

class UserListCreateApiView(APIView):
    def get(self,request):
        users=User.objects.all()
        serializer=UserSerializer(users,many=True)
        return Response(serializer.data)
    def post(self,request):
        serializer=UserSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=status.HTTP_201_CREATED)
        
class UserRetrieveUpdateView(APIView):
    def get(self,request,pk):
        users=get_object_or_404(User,pk=pk)
        serializer=UserSerializer(users)
        return Response(serializer.data)
    
    def put(self,request,pk):
        users=get_object_or_404(User,pk=pk)
        serializer=UserSerializer(users,data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
    
    def delete(self,request,pk):
        users=get_object_or_404(User,pk=pk)
        users.delete()
        return Response({"message":"Deleted Successfully"},status=status.HTTP_204_NO_CONTENT)
    
class TaskListCreateApi(APIView):
    def get(self,request):
        tasks=Task.objects.all()
        serializer=TaskSerializer(tasks,many=True)
        return Response(serializer.data)
    def post(self,request):
        serializer=TaskSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=status.HTTP_201_CREATED)
        
class TaskRetrieveUpdateApiView(APIView):
    def get(self,request,pk):
        tasks=get_object_or_404(Task,pk=pk)
        serializer=TaskSerializer(tasks)
        return Response(serializer.data)
    
    def put(self,request,pk):
        tasks=get_object_or_404(Task,pk=pk)
        serializer=TaskSerializer(tasks,data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
    
    def delete(self,request,pk):
        tasks=get_object_or_404(Task,pk=pk)
        tasks.delete()
        return Response({"message":"Deleted Successfully"},status=status.HTTP_204_NO_CONTENT)
    
    def tasks_status(request,status):
        valid_statuses = ['pending', 'in_progress', 'completed']
    
        if status not in valid_statuses:
            return Response({"error": "Invalid status provided"}, status=rest_status.HTTP_400_BAD_REQUEST)

        tasks=Task.objects.filter(status=status)
        serializer=TaskSerializer(tasks,many=True)
        return Response(serializer.data)