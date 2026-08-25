from rest_framework import serializers

from .models import Producto, Categoria


class CategoriaSerializer(serializers.ModelSerializer):

    class Meta:
        model = Categoria
        fields = [
            'id',
            'nombre'
        ]


class ProductoSerializer(serializers.ModelSerializer):

    class Meta:
        model = Producto
        fields = [
            'id',
            'nombre',
            'precio',
            'categoria'
        ]

    def validate_precio(self, value):

        if value <= 0:
            raise serializers.ValidationError(
                "El precio debe ser mayor que 0."
            )

        return value

    def validate_nombre(self, value):

        if not value.strip():
            raise serializers.ValidationError(
                "El nombre no puede estar vacío."
            )

        return value