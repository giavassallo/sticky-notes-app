"""
Views for Notes Apllication

Contains view functions responsible for handling CRUD ops for Note Objects
"""
from django.shortcuts import render, redirect, get_object_or_404
from .models import Note
from .forms import NoteForm 

"""
Displaying list of all notes in order by creation

Args:
    request (HTTPRequest): HTTP request
Returns:
    HTTPResponse: note list with note contexts
"""
def note_list(request):
    notes = Note.objects.all().order_by('-created_at')
    return render(request, 'notes/note_list.html', {'notes': notes})

"""
Creating new Note

Displays empty form (GET) and processing form submission(POST)

Args:
    request (HTTPRequest): HTTP request
Returns:
    HTTPResponse: redriect note list on success or
    render note form template on fail
"""
def note_create(request):
    if request.method == 'POST':
        form = NoteForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('note_list')
    else:
        form = NoteForm()
    return render(request, 'notes/note_form.html', {'form': form})

"""
Update existing Note

Args: 
    request (HTTPRequest): HTTP request
    pk (int): primary key of note to update
Returns: 
    HTTPResponse: redirect to note list on succes
    or render note form template with existing data
"""
def note_update(request, pk):
    note = get_object_or_404(Note, pk=pk)
    if request.method == 'POST':
        form = NoteForm(request.POST, instance=note)
        if form.is_valid():
            form.save()
            return redirect('note_list')
    else:
        form = NoteForm(instance=note)
    return render(request, 'notes/note_form.html', {'form': form})

"""
Delete existing Note

Args:
    request (HTTPRequest): HTTP request
    pk (int): primary key of note to delete
Returns:
    HTTPResponseRedirect: redirect to note list page
"""
def note_delete(request, pk):
    note = get_object_or_404(Note, pk=pk)
    note.delete()
    return redirect('note_list')
