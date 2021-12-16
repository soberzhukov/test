from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet

from app.models import CustomUser, Project
from app.serializers import CustomUserSerializer, ProjectSerializer


class CustomUserViewSet(ModelViewSet):
    queryset = CustomUser.objects.all()
    serializer_class = CustomUserSerializer


class ProjectViewSet(ModelViewSet):
    queryset = Project.objects.all()
    serializer_class = ProjectSerializer

