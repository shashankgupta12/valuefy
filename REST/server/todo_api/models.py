# todo_api/models.py

from django.db import models


class Todo(models.Model):

    """This class represents the todo model."""

    title = models.CharField(max_length=255, blank=False, unique=True)
    date = models.CharField(max_length=255, blank=False)
    description = models.CharField(max_length=255, blank=False)

    def __str__(self):

        """Return a human readable representation of the model instance."""

        return "{}, {}, {}".format(self.title, self.date, self.description)
