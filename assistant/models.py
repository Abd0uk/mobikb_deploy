from ckeditor.fields import RichTextField
from django.db import models

# Create your models here.
class Topic(models.Model):
    name = models.CharField(max_length=255, null=False)
    
    def __str__(self):
        return self.name

class Case(models.Model):
    name = models.CharField(max_length=255, null=False)
    topic = models.ForeignKey(Topic, on_delete=models.CASCADE)
    
    def __str__(self):
        return self.name

class Resolution(models.Model):
    name = models.CharField(max_length=255, null=False, default='<Temp_Value>')
    # resolve = models.TextField(max_length=3000, null=False)
    resolve = RichTextField()
    case = models.ForeignKey(Case, on_delete=models.CASCADE)
    
    def __str__(self):
        return self.name