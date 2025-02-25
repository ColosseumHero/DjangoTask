from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User

class Category(models.Model):
    title = models.CharField(max_length=255)
    created_at = models.DateField(default=timezone.now)

    def __str__(self):
        return  self.title

class Event(models.Model):
    title = models.CharField(max_length=255)
    description = models.CharField(max_length=300)
    date = models.DateField()
    location = models.CharField(max_length=255)
    organizer = models.CharField(max_length=255)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE, default=1)

    def __str__(self):
        return  self.title + ' | ' + self.organizer


