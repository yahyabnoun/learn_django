from django.db import models

# Create your models here.


class Famale(models.Model):
    name = models.CharField(max_length=255)
    def __str__(self) :
        return self.name

class Male(models.Model):
    name = models.CharField(max_length=255)
    girl = models.OneToOneField(Famale, on_delete=models.CASCADE)
    def __str__(self) :
        return self.name

