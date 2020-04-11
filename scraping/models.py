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


class Job(models.Model):
    url = models.TextField(null=True)
    title = models.TextField(null=True)
    company_name = models.TextField(null=True)
    location = models.TextField(null=True)
    industry = models.TextField(null=True)
    date_created = models.DateField(null=True)
