# to get data from website

from django.shortcuts import render
from .models import Code
from .serializers import CodeSerializer
from rest_framework import viewsets
# Create your views here.

class CodeView(viewsets.ModelViewSet):
    queryset=Code.objects.all()
    serializer_class=CodeSerializer
