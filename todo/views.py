from django.shortcuts import render, redirect
from django.views.generic import ListView, CreateView
from django.contrib import messages
from .models import Todo
from .forms import TodoForm

# Create your views here.

""" class Home(ListView):
    model = Todo
    context_object_name = "tasks"
    template_name="todo/home.html"

class createTask(CreateView):
    model = Todo
    form_class=TodoForm
    success_url="home"
    template_name = "todo/create_task.html"
 """
    
def home(request):
    tasks = Todo.objects.all()
    form = TodoForm()

    if request.method == "POST":
        form = TodoForm(request.POST)
        if form.is_valid():
            form.save()
        return redirect("home")
    
    context = {'tasks':tasks, 'form':form}

    return render(request, "todo/home.html", context)


def deleteTask(request, id):
    task = Todo.objects.get(id=id)
    if request.method == "POST":
        task.delete()
        messages.success(request,"Tarea borrada con éxito")
        return redirect("home")
    return render(request, "todo/delete_task.html", {"task":task})
        

def editTask(request, id):
    task = Todo.objects.get(id = id)
    if request.method == "GET":
        print("POST")
        task_form = TodoForm(instance=task)
    else:
        print("ERROR")
        task_form = TodoForm(request.POST ,instance=task)
        task_form.save()
        messages.success(request,"Se actualizó la tarea correctamente")
        return redirect("home")
    return render(request, "todo/edit_task.html", {"task":task_form})