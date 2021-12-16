
from rest_framework import serializers

from app.models import Project, CustomUser, UserProject


class UserProjectSerializer(serializers.ModelSerializer):

    class Meta:
        model = UserProject
        fields = ('id', 'user_id')


class CustomUserSerializer(serializers.ModelSerializer):

    class Meta:
        model = CustomUser
        fields = "__all__"


class ProjectSerializer(serializers.ModelSerializer):
    positions = UserProjectSerializer(many=True)

    class Meta:
        model = Project
        fields = ['json']

    def create(self, validated_data):
        positions = validated_data.pop('positions')

        project = super().create(validated_data)

        for position in positions:
            UserProject.objects.create(product_id=project, **position)

        return project

    def update(self, instance, validated_data):
        positions = validated_data.pop('positions')

        project = super().update(instance, validated_data)

        for position in positions:
            UserProject.objects.update_or_create(product_id=project, user_id=position["user_id"], defaults={**position})

        return project
