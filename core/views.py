from django.http import Http404
from django.shortcuts import redirect, render
from .forms import TaskForm
from .models import Task

from django.urls import reverse_lazy
from django.views import View
from django.views.generic.edit import DeleteView, UpdateView
from django.contrib.auth.mixins import LoginRequiredMixin


class HomeView(LoginRequiredMixin, View):
    template_name = 'core/home.html'
    
    def setup(self, request, *args, **kwargs):
        super().setup(request, *args, **kwargs)

        tasks = Task.objects.filter(owner=self.request.user).order_by('date_added')
        self.context = {
            'tasks': tasks,
            'form': TaskForm(request.POST or None),
        }
        
    def get(self, request, *args, **kwargs):
        return render(request, self.template_name, self.context)
    
    def post(self, request, *args, **kwargs):
        form = self.context['form']
        
        if not form.is_valid():
            return render(request, self.template_name, self.context)

        task = form.save(commit=False)
        
        if request.user.is_authenticated:
            task.owner = request.user
        
        form.instance.user = self.request.user
        form.save()
        return redirect('home')
            
class TaskUpdateView(LoginRequiredMixin, UpdateView):
    model = Task
    template_name = 'core/update.html'
    fields = ['task', 'complete']
    success_url = reverse_lazy('home')
    
    def get(self, request, pk):
        task = Task.objects.get(id=pk)
        
        if task.owner != request.user:
            raise Http404
        
        form = TaskForm(instance=task)
        context = {
            'form':form,
            }

        return render(request, self.template_name, context)


class TaskDeleteView(LoginRequiredMixin, DeleteView):
    model = Task
    template_name = 'core/delete.html'
    success_url = reverse_lazy('home')


"""
# Functions Based Views
def home(request):
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

def delete(request, pk):
    task = Task.objects.get(id=pk)
    
    if request.method == 'POST':
        task.delete()
        return redirect('home')

    context = {'task': task}
    return render(request, 'core/delete.html', context)

# Generic Based Views
class HomeFormView(LoginRequiredMixin, FormView):
    template_name = 'core/home.html'
    form_class = TaskForm
    success_url = reverse_lazy('home')
    
    def get_context_data(self, **kwargs):
        context = super(HomeFormView, self).get_context_data(**kwargs)
        context['tasks'] = Task.objects.order_by('date_added').all()
        #context['tasks'] = Task.Objects.filter(owner=self.request.user).order_by('date_added')
        return context

    def form_valid(self, form,*args, **kwargs):
        form.instance.user = self.request.user
        form.save(form.instance.user)
        return super(HomeFormView, self).form_valid(form, *args, **kwargs)
    
    def form_invalid(self, form, *args, **kwargs):
        return super(HomeFormView, self).form_invalid(form, *args, **kwargs)

class TaskUpdateView(LoginRequiredMixin, UpdateView):
    model = Task
    template_name = 'core/update.html'
    fields = ['task']
    success_url = reverse_lazy('home')
    
class TaskUpdateView(LoginRequiredMixin, View):
    template_name = 'core/update.html'
    
    def get(self, request, pk):
        task = Task.objects.get(id=pk)
        
        if task.owner != request.user:
            raise Http404
        
        form = TaskForm(instance=task)
        context = {
            'form':form,
            }
        
        return render(request, self.template_name, context)
    
    def post(self, request, pk):
        task = Task.objects.get(id=pk)
        task.task=request.POST.get('task')
        task.save()
        
        return redirect('home')
"""