from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse, HttpResponseForbidden
from .models import Task
from .forms import TaskForm
from rest_framework.permissions import AllowAny


from rest_framework import viewsets, permissions
from rest_framework.response import Response
from rest_framework.decorators import action
from django.contrib.auth.models import User
from .models import Task
from .serializers import TaskSerializer, UserSerializer

# User Registration
def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            login(request, user)
            return redirect('task_list')
    else:
        form = UserCreationForm()
    return render(request, 'register.html', {'form': form})

from django.db.models import Q

# Task List
@login_required
def task_list(request):
    tasks = Task.objects.filter(Q(owner=request.user) | Q(assigned_to=request.user))
    return render(request, 'task_list.html', {'tasks': tasks})


# Task Detail
@login_required
def task_detail(request, pk):
    task = get_object_or_404(Task, pk=pk)
    if task.owner != request.user and task.assigned_to != request.user:
        return HttpResponseForbidden("You are not allowed to view this task.")
    return render(request, 'task_detail.html', {'task': task})


# Create Task
@login_required
def task_create(request):
    if request.method == 'POST':
        form = TaskForm(request.POST)
        if form.is_valid():
            task = form.save(commit=False)
            task.owner = request.user
            task.save()
            return redirect('task_list')
    else:
        form = TaskForm()
    return render(request, 'task_form.html', {'form': form})

# Update Task
# @login_required
@login_required
def task_update(request, pk):
    task = get_object_or_404(Task, pk=pk)
    
    # Check if the user is the creator or the assigned user
    if request.user != task.owner and request.user != task.assigned_to:
        return HttpResponseForbidden("You do not have permission to edit this task.")
    
    if request.method == 'POST':
        form = TaskForm(request.POST, instance=task)
        if form.is_valid():
            form.save()
            return redirect('task_list')
    else:
        form = TaskForm(instance=task)
    return render(request, 'task_form.html', {'form': form})

# Delete Task
@login_required
def task_delete(request, pk):
    task = get_object_or_404(Task, pk=pk)
    
    # Check if the user is the creator
    if request.user != task.owner:
        return HttpResponseForbidden("You do not have permission to delete this task.")
    
    if request.method == 'POST':
        task.delete()
        return redirect('task_list')
    return render(request, 'task_confirm_delete.html', {'task': task})



# ######################################

class UserViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer

class TaskViewSet(viewsets.ModelViewSet):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer
    permission_classes = [AllowAny]  #