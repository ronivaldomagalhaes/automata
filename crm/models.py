from django.db import models

# Create your models here.
class Cadastro(models.Model):
	nome = models.CharField(max_length=15)
	sobrenome = models.CharField(max_length=15)
	apelido = models.CharField(max_length=15)
	
