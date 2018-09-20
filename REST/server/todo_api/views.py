# todo_api/views.py

from rest_framework import generics
from .serializers import TodoSerializer
from .models import Todo


class CreateView(generics.ListCreateAPIView):

    """This class defines the create behavior of the rest api."""

    queryset = Todo.objects.all()
    serializer_class = TodoSerializer

    def perform_create(self, serializer):

        """Save the post data when creating a new todo."""

        serializer.save()


class DetailsView(generics.RetrieveUpdateDestroyAPIView):

    """This class handles the http GET, PUT and DELETE requests."""

    queryset = Todo.objects.all()
    serializer_class = TodoSerializer
