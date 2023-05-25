from django.shortcuts import render
from rest_framework import viewsets
from api.models import Demo_Model
from api.serializers import Demo_serializer

class Demo_viewset(viewsets.ModelViewSet):
    queryset = Demo_Model.objects.all()
    serializer_class = Demo_serializer
    lookup_field = 'name'