from django.shortcuts import render,redirect
from  .models import Note
from django.contrib.auth import decorators
from .import forms
# Create your views here.





@decorators.login_required
def home(request):
    if request.method=='POST':
        id=request.POST.get('note_id')
        owner=request.user
        try:
            note=Note.objects.get(owner=owner,id=id)
            note.completed=True
            note.save()
        except:
            return redirect('all-notes')
        return redirect('all-notes')    
        
        

    owner=request.user
    notes=Note.objects.filter(owner=owner,completed=False)
    context={'notes':notes}
    return(render(request,'todo/home.html',context))

def noteView(request,noteid):
    note=Note.objects.get(owner=request.user,id=noteid)
    context={'note':note}
    return render(request,'todo/note.html',context)
def createnote(request):
    if request.method=='POST':
        print(request.POST.get('task'))
    form=forms.noteForm()
    context={'form':form}
    return render(request,'todo/deletenote.html',context)

@decorators.login_required
def allNotes(request):
    if request.method=='POST':
        id=request.POST.get('note_id')
        owner=request.user
        try:
            note=Note.objects.get(owner=owner,id=id)
            note.completed=True
            note.save()
        except:
            return redirect('all-notes')
        return redirect('all-notes')   
    owner=request.user
    notes=Note.objects.filter(owner=owner)
    context={'notes':notes}
    return(render(request,'todo/mynotes.html',context)) 
        