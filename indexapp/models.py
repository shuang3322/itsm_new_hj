from django.db import models

# Create your models here.
class IPdata(models.Model):
    position = models.CharField(max_length = 30)
    extension = models.CharField(max_length = 30)
    ip = models.GenericIPAddressField()
