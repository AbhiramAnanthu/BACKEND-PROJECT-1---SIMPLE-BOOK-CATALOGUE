from django.shortcuts import render
from .models import BookData as BookModel
from .api.serializers import BookDataSerializer
from rest_framework.decorators import APIView
from rest_framework.response import Response
from rest_framework import status
import uuid

class BookData(APIView):
    def get(self,request):
        id = request.query_params.get('id',None)
        book_data = BookModel.objects.filter(book_id = id)
        for book in book_data:
            serializer = BookDataSerializer(book)
            return Response(serializer.data)

    def post(self,request):
        serializer = BookDataSerializer(data=request.data)
        if serializer.is_valid():
            id = uuid.uuid4()
            instance = serializer.create(
                validated_data={**serializer.validated_data,"book_id":id}
            )
            instance.save()
            response_serializer = BookDataSerializer(instance)
            return Response(response_serializer.data,status=status.HTTP_200_OK)
        return Response(serializer.error,status=status.HTTP_400_BAD_REQUEST)