from django.contrib import admin

# Register your models here.
from .models import Usuario  # Asegúrate de importar tu modelo Usuario

admin.site.register(Usuario)
