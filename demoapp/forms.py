from django import forms
from .models import Task
from django.contrib.auth.models import User

class TaskForm(forms.ModelForm):
    class Meta:
        model = Task
        fields = ['title', 'description', 'assigned_to']
        widgets = {
            'assigned_to': forms.Select(choices=[(user.id, user.username) for user in User.objects.all()]),
        }
