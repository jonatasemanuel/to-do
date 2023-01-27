from django.http import HttpResponse
from django.shortcuts import redirect, render
from .forms import TaskForm
from .models import Task
# from django.contrib.auth.decorators import login_required


# Create your views here.
def new_task(request):
    if request.method != 'POST':
        form = TaskForm()
    else:
        form = TaskForm(request.POST)
        if form.is_valid():
            form = form.save(commit=False)
            #new_task.owner = request.user
            form.save()
            form = TaskForm()

    tasks = Task.objects.order_by('date_added').all()
    context = {'form': form, 'tasks': tasks}
    return render(request, 'core/home.html', context)


def edit_task(request, task_id):
    task = Task.objects.get(id = task_id)
    form = TaskForm(instance=task)

    if request.method == 'POST':
        form = TaskForm(request.POST, instance=task)
        if form.is_valid():
            form.save()
            return redirect('new_task')

    context = {'form': form}
    return render(request, 'core/edit_task.html', context)


def delete(request, task_id):
    task = Task.objects.get(id = task_id)
    
    if request.method == 'POST':
        task.delete()
        return redirect('new_task')

    context = {'task': task}
    return render(request, 'core/delete.html', context)