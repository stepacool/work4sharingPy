from django.db import models

# Create your models here.

STATUS_CHOICES = [
    ('active', 'active'),
    ('archive', 'archive'),
]


class Employee(models.Model):
    position = models.CharField(max_length=255)

    def __str__(self):
        return self.position


class Job(models.Model):
    url = models.TextField(null=True)
    title = models.TextField(null=True)
    company_name = models.TextField(null=True)
    location = models.TextField(null=True)
    industry = models.TextField(null=True)
    date_created = models.DateField(null=True)

    def __str__(self):
        return self.title + " " + self.company_name + " " + self.location
