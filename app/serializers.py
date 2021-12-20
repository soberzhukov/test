
from rest_framework import serializers
from rest_framework.exceptions import ValidationError

from app.models import Project, CustomUser


class CustomUserSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = CustomUser
        fields = ['id', 'email', 'username', 'push_token']
        read_only_field = []


class ProjectSerializer(serializers.ModelSerializer):

    class Meta:
        model = Project
        fields = ['id', 'json', 'users']

    def validate_json(self, value):
        if not value.get("project_name", None):
            raise ValidationError('Должно быть поле project_name')
        return value

    def create(self, validated_data):
        validated_data = {**validated_data, 'projectname': validated_data.get('json').get("project_name")}

        users = validated_data.pop('users')
        project = super().create(validated_data)

        for user in users:
            project.users.add(user)

        return project

    def update(self, instance, validated_data):
        validated_data = {**validated_data, 'projectname': validated_data.get('json').get("project_name")}

        users = validated_data.pop('users')
        project = super().update(instance, validated_data)
        for user in users:
            project.users.set([user])

        return project
