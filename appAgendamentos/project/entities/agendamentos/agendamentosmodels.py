from django.db import models

# Create your models here.

class Agendamento(models.Model):
    nomemedico = models.CharField(max_length=250)
    nomepaciente = models.CharField(max_length=250)
    data = models.CharField(max_length=15)
    horario = models.CharField(max_length=15)
    email = models.CharField(max_length=250)
