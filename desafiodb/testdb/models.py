from django.db import models

# Create your models here.
class Persona(models.Model):
    id = models.AutoField(primary_key=True)
    campo1 = models.CharField(max_length=100)
    valor1 = models.IntegerField()