from django.db import models
from django.forms import IntegerField


class Biblioteca(models.Model):
	titulo = models.CharField(max_length=50)
	autor = models.CharField(max_length=30)
	paginas = IntegerField()
		
	def __str__(self):
		return self.titulo