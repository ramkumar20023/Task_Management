from rest_framework import serializers
from .models import User,Task

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model=User
        fields='__all__'

class TaskSerializer(serializers.ModelSerializer):
    class Meta:
        model=Task
        fields='__all__'

    def validate_status(self, value):
        valid_statuses = ['pending', 'in_progress', 'completed']
        if value not in valid_statuses:
            raise serializers.ValidationError("Invalid status. Choose from 'pending', 'in_progress', or 'completed'.")
        return value