# tasks/serializers.py

from rest_framework import serializers
from .models import Task


class TaskCreateSerializer(serializers.ModelSerializer):

    class Meta:
        model = Task

        fields = [
            "title",
            "description",
            "priority",
            "assigned_to",
            "due_date"
        ]

    def validate_due_date(self, value):

        from datetime import date

        if value < date.today():
            raise serializers.ValidationError(
                "Due date cannot be past date"
            )

        return value