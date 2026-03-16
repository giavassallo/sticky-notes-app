"""
Models for Notes App

Defines database schema for note storing
"""

from django.db import models

"""
Respresents single note in app

Attributes:
    title(str): title of note
    comtent(str): main text of note
    Created_at(datetime): atuo timestamp when note is created
"""
class Note(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        """
        Return a readable string of the note

        Return:
            str: title of note
        """
        return self.title
