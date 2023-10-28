from usuario.models import Usuario
from rest_framework import serializers

class projectSerializer(serializers.ModelSerializer):
    class Meta:
        model = Usuario
        fields = (
            'id_usuario',
            'email',
            'nombres',
            'dpi',  
            'password',
            'is_active',
            'is_staff',
        )
