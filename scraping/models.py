from django.db import models

# Create your models here.

STATUS_CHOICES = [
    ('active', 'active'),
    ('archive', 'archive'),
]

class Employee(models.Model):
    name = models.CharField(max_length=511)
    position = models.CharField(max_length=255)
    status = models.CharField(choices=STATUS_CHOICES, max_length=7)
    description = models.TextField()
