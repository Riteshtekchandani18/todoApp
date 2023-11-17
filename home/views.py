from django.shortcuts import render

# Create your views here.
def index(request):
    context = {}
    return render(request,'index.html',context)

def add_task(request):
    context = {}
    return render(request,'todo_list.html ',context)

def update_task(request):
    context ={ }
    return render(request , 'todo_list.html',context)