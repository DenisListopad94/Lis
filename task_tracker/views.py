from email.policy import default
from time import sleep

from django.shortcuts import render,redirect
from .models import Task
from .forms import TaskModelForm
from django.views.decorators.cache import cache_page


@cache_page(60 * 30)
def show_all_tasks(request):
    tasks = Task.objects.prefetch_related("comments__task").prefetch_related("tags__tasks").select_related(
        "project").all() # тут делаем задачи в админ из базы
    context = {
        "tasks": tasks,
    }
    sleep(4)

    return render(request, "tasks.html", context=context)


def create_task_form(request):
    context = {}
    # form = TaskForm()
    if request.method == "POST":

        form = TaskModelForm(request.POST, request.FILES)

        form.save()

        if form.is_valid():
            context["form"] = form

            return redirect("all_tasks")
    else:
        form = TaskModelForm()
        context["form"] = form

    return render(request, "task_form.html", context=context)