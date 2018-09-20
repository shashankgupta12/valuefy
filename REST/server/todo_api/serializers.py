# todo_api/serializers.py

from rest_framework import serializers
from .models import Todo


class TodoSerializer(serializers.ModelSerializer):

    """Serializer to map the Model instance into JSON format."""

    class Meta:

        """Meta class to map serializer's fields with the model fields."""

        model = Todo
        fields = ('id', 'title', 'date', 'description')
