from django.db import models

# Create your models here.

class Marca (models.Model):
	nombre		= models.CharField(max_length = 50)

	def __unicode__ (self):
		return self.nombre

class Color (models.Model):
	nombre		= models.CharField(max_length = 50)

	def __unicode__ (self):
		return self.nombre

class Material (models.Model):
	nombre	= models.CharField(max_length = 70)

	def __unicode__ (self):
		return self.nombre

class Talla (models.Model):
	medida_americana	= models.CharField(max_length = 70)
	medida_nacional		= models.CharField(max_length = 70)

	def __unicode__ (self):
		return self.medida_nacional

class Modelo (models.Model):
	nombre	= models.CharField(max_length = 70)
	descripcion	=  models.TextField(max_length = 70)

	def __unicode__ (self):
		return self.nombre
		
class Zapatos(models.Model):

	def url(self, filename):
		ruta ="MultimediaData/zapatos/%s/%s"%(self.marca, str(filename))
		return ruta

	marca           = models.ForeignKey(Marca)
	modelo			= models.ForeignKey(Modelo)
	color           = models.ManyToManyField(Color)
	material        = models.ManyToManyField(Material)
	talla			= models.ManyToManyField(Talla)
	cantidad        = models.IntegerField()
	imagen			= models.ImageField(upload_to = url, null = True, blank = True)
	precio			= models.IntegerField()
	importado		= models.BooleanField()

	def __unicode__ (self):
		return self.marca
	






