from django.db import models
from django.contrib.auth.models import User

class Status(models.Model):
    name = models.CharField(max_length=100, unique=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = "statuses"

class Category(models.Model):
    name = models.CharField(max_length=100, unique=True)

    def __str__(self):
        return self.name

class Task(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField(blank=True)
    assignee = models.ForeignKey(User, on_delete=models.CASCADE, related_name='tasks', null=True, blank=True)
    category = models.ForeignKey(Category, on_delete=models.SET_NULL, related_name='tasks', null=True, blank=True)
    status = models.ForeignKey(Status, on_delete=models.PROTECT, related_name='tasks')

    def __str__(self):
        return self.title
