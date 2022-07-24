from django.http import HttpResponse , HttpRequest
from django.shortcuts import render ,redirect
from . models import Todo
# Create your views here.
def listview(request):
    context = {'home': Todo.objects.all()}
    return render(request,'home.html',context)

def inserttodo(request:HttpRequest):
    todos = Todo(content = request.POST['content'])
    todos.save()
    return redirect('/')

def delete_todo_item(request,todo_id):
    todo_to_delete = Todo.objects.get(id = todo_id)
    todo_to_delete.delete()
    return redirect('/')
