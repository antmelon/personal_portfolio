from django.db import models

# Create your models here.
class Header(models.Model):
    image = models.FilePathField(path="/img")
