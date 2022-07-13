from django.db import models

# Create your models here.

class Deporte(models.Model):
    nombre = models.CharField(max_length=50)
    categoria= models.CharField(max_length=50)

    def __str__(self):
        return self.nombre+" "+str(self.categoria)

class Socio(models.Model):
    nombre= models.CharField(max_length=50)
    apellido= models.CharField(max_length=50)
    email= models.EmailField()
    numero_socio=models.CharField(max_length=50)
    numero_dni=models.CharField(max_length=50)
    nacimiento=models.DateField(max_length=50)
    deporte=models.CharField(max_length=50)
    categoria=models.CharField(max_length=50)
    

    def __str__(self):
        return self.nombre+" "+self.apellido

class Profesor(models.Model):
    nombre= models.CharField(max_length=50)
    apellido= models.CharField(max_length=50)
    email= models.EmailField()
    deporte= models.CharField(max_length=50)
    categoria= models.CharField(max_length=50)
    nacimiento=models.CharField(max_length=50)
   
    def __str__(self):
        return self.nombre+" "+self.apellido