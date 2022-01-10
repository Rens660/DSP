from django.db import models
from django.db.models.base import Model

# Create your models here.
class Upload(models.Model):
    file = models.FileField()
    title = models.CharField(max_length=255)
    case_nr = models.CharField(max_length=255)
    description = models.TextField()
    date = models.DateTimeField(auto_now=True)
    crime_type = models.CharField(max_length=255)

    def __str__(self):
        return self.title