from django.shortcuts import render
from tasks.models import Task, Category
from django.db.models import Q
from tasks.forms import SearchForm, TaskForm, TaskForm2
from django.http import HttpResponse
# Create your views here.

def list_tasks(request):
    if request.method == "GET":
        search = request.GET.get('search', None)
        category = request.GET.get('category', None)
        ordering = request.GET.get('ordering', None)
        tasks = Task.objects.all()
        if search:
            tasks = tasks.filter (Q(title__icontains=search) | Q(description__icontains=search))
        if category:
            tasks = tasks.filter(category__id__in=tasks)
        form = SearchForm()
        context = {'tasks': tasks, 'form': form}
        return render(request, 'tasks/list_view.html', context=context)

def create_tasks(request):
    if request.method == 'GET':
        form = TaskForm()
        return render(request, 'tasks/task_create.html', context={'form': form})
    if request.method == 'POST':
        form = TaskForm2(request.POST, request.FILES)
        if not form.is_valid():
            return render(request, 'tasks/task_create.html', {'form': form})
        form.save()
        return HttpResponse(f'Created task')

def detail_tasks(request, task_id):
    task = Task.objects.get(id=task_id)
    return render(request, 'tasks/task_detail.html', {'task': task})
