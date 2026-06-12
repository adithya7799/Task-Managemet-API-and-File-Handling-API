# apps/file_management/models.py

from django.db import models
from django.contrib.auth import get_user_model
from apps.tasks.models import Task

User = get_user_model()


class TaskFile(models.Model):

    task = models.ForeignKey(
        Task,
        on_delete=models.CASCADE,
        related_name="files"
    )

    file_name = models.CharField(
        max_length=255
    )

    file_size = models.IntegerField()

    file_type = models.CharField(
        max_length=50
    )

    s3_key = models.CharField(
        max_length=500
    )

    uploaded_by = models.ForeignKey(
        User,
        on_delete=models.CASCADE
    )

    created_at = models.DateTimeField(
        auto_now_add=True
    )