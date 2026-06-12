# services/s3_service.py

import boto3
import uuid


class S3Service:

    @staticmethod
    def upload_file(file, task_id):

        s3_client = boto3.client(
            "s3"
        )

        unique_name = (
            str(uuid.uuid4())
            + "_"
            + file.name
        )

        s3_key = (
            f"tasks/{task_id}/"
            f"{unique_name}"
        )

        s3_client.upload_fileobj(
            file,
            "my-company-bucket",
            s3_key
        )

        return s3_key