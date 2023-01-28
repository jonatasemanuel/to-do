from django.shortcuts import redirect, render
from django.urls import reverse_lazy
from .forms import TaskForm
from .models import Task
from django.views.generic import FormView, UpdateView, DeleteView
# from django.contrib.auth.decorators import login_required


class HomeFormView(FormView):
    template_name = 'core/home.html'
    form_class = TaskForm
    success_url = reverse_lazy('home')

    def get_context_data(self, **kwargs):
        context = super(FormView, self).get_context_data(**kwargs)
        context['tasks'] = Task.objects.order_by('date_added').all()
        return context
    
    def form_valid(self, form,*args, **kwargs):
        form.save()
        return super(HomeFormView, self).form_valid(form, *args, **kwargs)
    
    def form_invalid(self, form, *args, **kwargs):
        return super(HomeFormView, self).form_invalid(form, *args, **kwargs)


class TaskUpdateView(UpdateView):
    model = Task
    template_name = 'core/update.html'
    fields = ['task']
    success_url = reverse_lazy('home')


class TaskDeleteView(DeleteView):
    model = Task
    template_name = 'core/delete.html'
    success_url = reverse_lazy('home')
    


"""def delete(request, pk):
    task = Task.objects.get(id=pk)
    
    if request.method == 'POST':
        task.delete()
        return redirect('home')

    context = {'task': task}
    return render(request, 'core/delete.html', context)"""


"""
def new_task(request):
    if request.method == 'POST':
        form = TaskForm(request.POST)
        if form.is_valid():
            form = form.save(commit=False)
            #new_task.owner = request.user
            form.save()
            form = TaskForm()

    form = TaskForm()
    tasks = Task.objects.order_by('date_added').all()
    context = {'form': form, 'tasks': tasks}
    return render(request, 'core/home.html', context)
    
def edit(request, pk):
    task = Task.objects.get(id=pk)
    form = TaskForm(instance=task)

    if request.method == 'POST':
        form = TaskForm(request.POST, instance=task)
        if form.is_valid():
            form.save()
            return redirect('home')

    context = {'form': form}
    return render(request, 'core/update.html', context)

"""