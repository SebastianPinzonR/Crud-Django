from django.shortcuts import render, redirect
from .models import Task

# Create your views here.

def list_tasks(request):
    tasks = Task.objects.all()
    print(tasks)
    return render(request, 'list_task.html', {"tasks": tasks})

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

#funcion para eliminar una tarea
def delete_task(request, task_id):
    Task.objects.get(id=task_id).delete()
    return redirect('/tasks/')