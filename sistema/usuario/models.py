from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin
from django.utils import timezone


class CustomUserManager(BaseUserManager):
    def create_user(self, email, dpi, nombre,apellido, password=None, **extra_fields):
        if not email:
            raise ValueError('El Email es obligatorio')
        
        email = self.normalize_email(email)
        usuario = self.model(
            email=email,
            dpi=dpi,
            nombre=nombre,
            apellido=apellido,
            password=password,
            **extra_fields
        )
        usuario.set_password(password)
        usuario.save(using=self._db)
        return usuario

    def create_superuser(self, email, dpi, nombre,apellido, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)

        if extra_fields.get('is_staff') is not True:
            raise ValueError('Superuser debe tener is_staff=True.')
        if extra_fields.get('is_superuser') is not True:
            raise ValueError('Superuser debe tener is_superuser=True.')

        return self.create_user(email, dpi, nombre,apellido, password, **extra_fields)

class Usuario(AbstractBaseUser, PermissionsMixin):
    id_usuario = models.AutoField(primary_key=True)
    email = models.CharField(max_length=255, unique=True)
    nombre = models.CharField(max_length=255)
    apellido= models.CharField(max_length=255)
    dpi = models.CharField(max_length=13, unique=True)
    genero = models.CharField(max_length=10)
    escolaridad = models.CharField(max_length=100)
    telefono = models.IntegerField()
    direccion = models.CharField(max_length=100)
    etnia = models.CharField(max_length=100)
    fecha_nacimiento = models.DateField()
    edad = models.IntegerField()
    created_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now=True)

    
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False) 
    
    objects = CustomUserManager()
    class Meta:
        ordering = ['-created_at']
    
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['nombre','apellido',  'dpi']

    def has_perm(self, perm, obj=None):
        # Define aquí tu lógica para los permisos
        return True

    def has_module_perms(self, app_label):
        # Define aquí tu lógica para los permisos de módulo
        return True
    
class CategoriaCurso(models.Model):
    id_categoria = models.AutoField(primary_key=True)
    nombre_categoria = models.CharField(max_length=255)
    descripcion_categoria = models.TextField()

    class Meta:
        verbose_name = 'Categoría Curso'
        verbose_name_plural = 'Categorías Curso'

    def __str__(self):
        return self.nombre_categoria
    
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
    

