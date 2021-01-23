from rest_framework import serializers
from .models import Peoples

class Peoplesserializer(serializers.ModelSerializer):
    class Meta:
        model= Peoples
        fields=('id','name','sex','country')