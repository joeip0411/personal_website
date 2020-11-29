from django.db import models

# Create your models here.
class Project(models.Model):
    title = models.CharField(max_length=1000)
    description = models.TextField()
    technology = models.CharField(max_length=1000)
    image = models.ImageField(upload_to='images/',default=None, blank=True, null=True)
    link = models.CharField(max_length=1000, default=None, blank=True,null=True)
