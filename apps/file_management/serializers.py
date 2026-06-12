# serializers.py

from rest_framework import serializers


class FileUploadSerializer(
    serializers.Serializer
):

    task_id = serializers.IntegerField()

    file = serializers.FileField()

    def validate_file(self, file):

        allowed_extensions = [
            "pdf",
            "jpg",
            "png",
            "docx"
        ]

        ext = file.name.split(".")[-1]

        if ext not in allowed_extensions:
            raise serializers.ValidationError(
                "Invalid file type"
            )

        max_size = 10 * 1024 * 1024

        if file.size > max_size:
            raise serializers.ValidationError(
                "File too large"
            )

        return file