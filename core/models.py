from django.db import models


# Create your models here.
class Task(models.Model):
    """Campo para o user colocar uma tarefa"""
    task = models.CharField(max_length=70)
    date_added = models.DateField(auto_now_add=True)
    # owner = models.ForeingKey(User, on_delete=models.CASCADE) 
    # importar dj.contrib.auth.models import user
    def __str__(self) -> str:
        return self.task[:37]
