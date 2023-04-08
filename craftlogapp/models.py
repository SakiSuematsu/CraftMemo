from django.db import models

# Create your models here.


class CraftlogModel(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    author = models.CharField(max_length=50)
    filetype = models.TextField(default='picture')
    storage  = models.TextField(null=True, blank=True)
    craftimage = models.FileField(upload_to='craftimage')
