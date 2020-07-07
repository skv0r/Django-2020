from django.shortcuts import render, redirect
from .models import Task
from .forms import TaskForm


def index(request):
    tasks = Task.objects.order_by('-id')[:1]
    return render(request, 'Body/index.html', {'title': 'Главная страница сайта', 'tasks': tasks})


def about(request):
    return render(request, 'Body/about.html')

def create(request):
    if request.method == 'POST':
        form = TaskForm(request.POST)
        error = ''
        if form.is_valid():
            form.save()
            return redirect('home')
        else:
            error = 'Форма оказалась неверной'

    form = TaskForm()
    context = {
        'form': form
    }
    return render(request, 'Body/create.html', context)
