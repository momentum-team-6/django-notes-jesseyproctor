from django.shortcuts import render
from .data import NOTES
from .models import Note

# Create your views here.
def notes_list(request):
    notes = Note.objects.all()
    return render(request, "core/index.html", {"notes":notes})

def note_detail(request, pk):
    note = get_object_or_404(Note, pk=pk)
    return render(request, "core/note_detail.html", {"note": note})

def add_note(request):
    if request.method == 'GET':
        form = NoteForm()
    else:
        form = NoteForm(data=request.POST)
        if form.is_valid():
            form.save()
            return redirect(to='notes_list')
    return render(request, "core/add_note.html", {'form': form})

def edit_note(request, pk):
    note = get_object_or_404(Note, pk=pk)
    if request.method == 'GET':
        form = NoteForm(instance=note)
    else:
        form = NoteForm(data=request.POST, instance=note)
        if form.is_valid():
            form.save()
            return redirect(to='notes_list')
    return render(request, "core/edit_note.html", {
        "form": form,
        "note": note

    })

def delete_note(request, pk):
    note = get_object_or_404(Note, pk=pk)
    if request.method == 'POST':
        note.delete()
        return redirect(to='notes_list')

    return render(request,'core/delete_note.html', {'note': note})
