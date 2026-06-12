# views.py

class FileUploadAPIView(
    APIView
):

    def post(self, request):

        serializer = (
            FileUploadSerializer(
                data=request.data
            )
        )

        serializer.is_valid(
            raise_exception=True
        )

        file = FileService.upload_file(
            serializer.validated_data,
            request.user
        )

        return Response(
            {
                "message":
                    "File uploaded",
                "id": file.id
            }
        )