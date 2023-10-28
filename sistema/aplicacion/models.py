from django.db import models
from usuario.models import Usuario

# Create your models here.



#---------------CATEGORIA CURSO---------------
class CategoriaCurso(models.Model):
    id_categoria = models.AutoField(primary_key=True)
    nombre_categoria = models.CharField(max_length=255)
    descripcion_categoria = models.TextField()

    class Meta:
        verbose_name = 'Categoría Curso'
        verbose_name_plural = 'Categorías Curso'

    def __str__(self):
        return self.nombre_categoria

#---------------CURSO---------------
class Curso(models.Model):
    id_curso = models.AutoField(primary_key=True)
    nombre_curso = models.CharField(max_length=255)
    descripcion_curso = models.TextField()
    fecha_inicio = models.DateField()
    fecha_fin = models.DateField()
    duracion = models.IntegerField()
    horarios = models.CharField(max_length=255)
    establecimiento = models.CharField(max_length=255)
    costo = models.FloatField()
    cupos_disponibles = models.IntegerField()
    estado = models.BooleanField()
    id_categoria = models.ForeignKey(CategoriaCurso, on_delete=models.CASCADE)

    class Meta:
        verbose_name = 'Curso'
        verbose_name_plural = 'Cursos'

    def __str__(self):
        return self.nombre_curso


#---------------INSCRIPCIONES---------------



#-------------NOTIFICACION---------------


#----------------favoritos-------------


class Estudiante(models.Model):
    id_estudiante = models.AutoField(primary_key=True)
    dpi = models.CharField(max_length=14)
    nombre = models.CharField(max_length=50)
    genero = models.CharField(max_length=10)
    escolaridad = models.CharField(max_length=100)
    telefono = models.IntegerField()
    direccion = models.CharField(max_length=100)
    etnia = models.CharField(max_length=100)
    fecha_nacimiento = models.DateField()
    edad = models.IntegerField()
    id_curso = models.ForeignKey(Curso, on_delete=models.CASCADE)

    class Meta:
        verbose_name = 'Estudiante'
        verbose_name_plural = 'Estudiantes'

    def __str__(self):
        return self.dpi
    
class Inscripcion(models.Model):
    id_inscripcion = models.AutoField(primary_key=True)
    id_estudiante = models.ForeignKey(Estudiante, on_delete=models.CASCADE)
    id_curso = models.ForeignKey(Curso, on_delete=models.CASCADE)
    fecha_inscripcion = models.DateField()

    class Meta:
        verbose_name = 'Inscripción'
        verbose_name_plural = 'Inscripciones'

    def __str__(self):
        return f'{self.id_estudiante} - {self.id_curso}'
        
    
class Favorito(models.Model):
    id_favorito = models.AutoField(primary_key=True)
    id_estudiante = models.ForeignKey(Estudiante, on_delete=models.CASCADE)
    id_curso = models.ForeignKey(Curso, on_delete=models.CASCADE)

    class Meta:
        verbose_name = 'Favorito'
        verbose_name_plural = 'Favoritos'

class Notificacion(models.Model):
    id_notificacion = models.AutoField(primary_key=True)
    id_inscripcion = models.ForeignKey(Inscripcion, on_delete=models.CASCADE)
    mensaje = models.CharField(max_length=255)
    fecha_creacion = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = 'Notificación'
        verbose_name_plural = 'Notificaciones'

    def __str__(self):
        return self.mensaje