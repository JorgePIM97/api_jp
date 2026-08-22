from rest_framework import serializers
from .models import Producto


class ProductoSerializer(serializers.ModelSerializer):

    class Meta:
        model = Producto
        fields = ['id', 'nombre', 'precio']

    def validate_precio(self, value):

        if value <=0:
            raise serializers.ValidationError("El precio debe ser mayor que 0")

        return value


    def validate_nombre(self, value):

        if not value.strip():
            raise serializers.ValidationError(
                "El nombre no puede estar vacío."
            )

        return value