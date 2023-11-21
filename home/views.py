from django.shortcuts import render,redirect
from .models import Task
# Create your views here.
def index(request):
    context = {
        'task': Task.objects.all()
    }
    return render(request,'index.html',context)

def add_task(request):
    if request.method =='Post':
     Task = request.Post.get('task')
     if len(Task)>=2:
        Task.Objects.create(title=Task)
redirect('home')

def update_task(request,id):
    context ={ }
    return render(request , 'todo_list.html',context)

def delete_task(request,id):
    pass   