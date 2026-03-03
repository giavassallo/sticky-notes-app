"""
Forms for Note App

Defines forms used to create/update Note instances
"""
from django import forms
from .models import Note

"""
Form for creating/updating objects

Based on Note model and includes title and content fields
"""
class NoteForm(forms.ModelForm):
    """
    Meta config for NoteForm

    Attributes:
    model(model): model associated with form
    fields(list): fields included in form
    """
    class Meta:
        model = Note
        fields = ['title', 'content']
