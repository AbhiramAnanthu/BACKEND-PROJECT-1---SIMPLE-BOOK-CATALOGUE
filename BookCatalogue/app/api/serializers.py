from rest_framework import serializers
from ..models import *

class BookDataSerializer(serializers.ModelSerializer):
    class Meta:
        model = BookData
        fields = ['book_id','book_name','book_cover','book_status']
