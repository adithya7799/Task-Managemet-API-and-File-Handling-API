# tasks/services.py

from .models import Task


class TaskService:

    @staticmethod
    def create_task(validated_data, created_by):

        task = Task.objects.create(
            created_by=created_by,
            **validated_data
        )

        return task