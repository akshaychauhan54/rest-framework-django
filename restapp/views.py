from django.shortcuts import render
from .models import Peoples
from .serializers import Peoplesserializer
from rest_framework import viewsets

class Peoplesview(viewsets.ModelViewSet):
    queryset=Peoples.objects.all()
    serializer_class= Peoplesserializer
