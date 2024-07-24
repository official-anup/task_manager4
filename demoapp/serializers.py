from rest_framework import serializers
from django.contrib.auth.models import User
from .models import Task

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username']

class TaskSerializer(serializers.ModelSerializer):
    owner = UserSerializer(read_only=True)
    assigned_to = UserSerializer(read_only=True)

    class Meta:
        model = Task
        fields = ['id', 'title', 'description', 'created_at', 'updated_at', 'owner', 'assigned_to']
