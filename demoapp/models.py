from django.contrib.auth.models import User
from django.db import models

class Task(models.Model):
    title = models.CharField(max_length=100)
    
    description = models.TextField()
    
    created_at = models.DateTimeField(auto_now_add=True)
    
    updated_at = models.DateTimeField(auto_now=True)
    
    owner = models.ForeignKey(User, related_name='tasks', on_delete=models.CASCADE)
    
    assigned_to = models.ForeignKey(User, related_name='assigned_tasks', on_delete=models.SET_NULL, null=True, blank=True)

    def __str__(self):
        return self.title
