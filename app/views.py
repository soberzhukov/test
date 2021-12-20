from django.shortcuts import render
from rest_framework.permissions import IsAuthenticated
from rest_framework.viewsets import ModelViewSet

from app.models import CustomUser, Project
from app.serializers import CustomUserSerializer, ProjectSerializer


class CustomUserViewSet(ModelViewSet):
    queryset = CustomUser.objects.all()
    serializer_class = CustomUserSerializer
    # permission_classes = [IsAuthenticated]

    # def perform_create(self, serializer):
    #     pass


class ProjectViewSet(ModelViewSet):
    queryset = Project.objects.all()
    serializer_class = ProjectSerializer
    # permission_classes = [IsAuthenticated]

