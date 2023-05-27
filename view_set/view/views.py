from django.shortcuts import render
from rest_framework import status
from rest_framework import viewsets
from .serializers import StudentSerializer
from .models import Student
from rest_framework.response import Response
from rest_framework.generics import GenericAPIView,ListAPIView,CreateAPIView,RetrieveAPIView,DestroyAPIView,UpdateAPIView,ListCreateAPIView,RetrieveUpdateAPIView,RetrieveDestroyAPIView,RetrieveUpdateDestroyAPIView

# Create your views here.

class Student_viewset(viewsets.ViewSet):
    def list(self, request):
        # Note the use of `get_queryset()` instead of `self.queryset`
        stu=Student.objects.all()
        serializer = StudentSerializer(stu, many=True)
        return Response(serializer.data)


    def retrieve(self,request,pk=None):
        id=pk
        if id is not None:
            stu=Student.objects.get(id=id)
            serializer = StudentSerializer(stu)
            return Response(serializer.data)
    

    def create(self,request):
        serializer=StudentSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'msg':'Date Created'},status=status.HTTP_201_CREATED)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)


    def update(self,request,pk):
        id=pk
        stu=Student.objects.get(pk=id)
        serializer=StudentSerializer(stu,data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'msg':'Complete Data Updated'})
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
    

    def partial_update(self,request,pk):
        id=pk
        stu=Student.objects.get(pk=id)
        serializer=StudentSerializer(stu,data=request.data,partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response({'msg':'Complete Partial Data Updation'})
        return Response(serializer.errors)

    def destroy(self,request,pk):
        id=pk
        stu=Student.objects.get(pk=id)
        stu.delete()
        return Response({'msg':'Complete Data Deletion'})




