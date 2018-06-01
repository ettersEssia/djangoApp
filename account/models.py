from django.db import models
from django.utils import timezone
from django.conf import settings

# Create your models here.
class project(models.Model):
    name        = models.CharField(max_length=100, unique=True)
    owner       = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    description = models.TextField()
    create_date = models.DateTimeField(default=timezone.now)
    edit_date   = models.DateTimeField(default=timezone.now)

class pipe(models.Model):
    name    = models.CharField(max_length=100)
    type    = models.CharField(max_length=20, default="PIPE")
    length  = models.IntegerField()
    inDiam  = models.IntegerField()
    outDiam = models.IntegerField()
    color   = models.CharField(max_length=7)
    project = models.ForeignKey(project, on_delete=models.CASCADE)

class parallelepiped(models.Model):
    name    = models.CharField(max_length=100)
    type    = models.CharField(max_length=20, default="CUBE")
    length  = models.IntegerField()
    color   = models.CharField(max_length=7)
    project = models.ForeignKey(project, on_delete=models.CASCADE)
