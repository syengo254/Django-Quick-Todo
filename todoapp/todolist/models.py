from pyexpat import model
from django.db import models

# Create your models here.

class Todo(models.Model):
    title = models.CharField(max_length=200)
    completed = models.BooleanField(default=False)
    created = models.DateTimeField(auto_now=True)

    def __str__(self) -> str:
        return self.title[:20]
