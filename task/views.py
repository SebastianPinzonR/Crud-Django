from django.shortcuts import render, redirect
from .models import Task

# Create your views here.

def list_tasks(request):
    return render(request, 'list_task.html')

def create_task(request):
    #aqui no se castea el request.POST
    #aqui se puede validar si lanza una excepcion o extenderlo a otra vista
    Task(title = request.POST['title'],
         description = request.POST['description']).save()
    #aqui se castea el request.POST
    # task= Task(title = request.POST['title'],
    #      description = request.POST['description']).save()
    # task.save()
    return redirect('/tasks/')