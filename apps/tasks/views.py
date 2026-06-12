# tasks/views.py

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from .serializers import TaskCreateSerializer
from .services import TaskService


class TaskCreateAPIView(APIView):

    def post(self, request):

        serializer = TaskCreateSerializer(
            data=request.data
        )

        serializer.is_valid(
            raise_exception=True
        )

        task = TaskService.create_task(
            validated_data=serializer.validated_data,
            created_by=request.user
        )

        return Response(
            {
                "message": "Task created",
                "task_id": task.id
            },
            status=status.HTTP_201_CREATED
        )