from django.http import HttpResponse
from django.shortcuts import redirect, render

from .forms import *
from .models import *

# Create your views here.


def index(request):
    tasks = Task.objects.all()

    form = TaskFrom()

    if request.method == "POST":
        form = TaskFrom(request.POST)
        if form.is_valid():
            form.save()
        return redirect("/")

    context = {"tasks": tasks, "form": form}
    return render(request, "tasks/list.html", context)


def updateTask(request, pk):
    task = Task.objects.get(id=pk)

    form = TaskFrom(instance=task)

    if request.method == "POST":
        form = TaskFrom(request.POST, instance=task)
        if form.is_valid():
            form.save()
        return redirect("/")

    context = {"form": form}

    return render(request, "tasks/update_task.html", context)


def deleteTask(request, pk):
    item = Task.objects.get(id=pk)

    if request.method == "POST":
        item.delete()
        return redirect("/")

    context = {"item": item}
    return render(request, "tasks/delete.html", context)
