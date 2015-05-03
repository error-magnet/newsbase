from django.db import models

# Create your models here.
class NewsSource(models.Model):
    name = models.CharField(max_length=100)
    url = models.URLField()

class NewsCategory(models.Model):
    name = models.CharField(max_length=100)
    sources = models.ManyToManyField(NewsSource)