from django.db import models

class Institute(models.Model):
    name = models.CharField(max_length=100)
    photo = models.ImageField(upload_to='photos/%Y/%m/%d/')
    title = models.CharField(max_length=100)