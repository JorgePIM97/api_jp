from rest_framework import serializers

from .models import Producto, Categoria

class ProductoSimpleSerializer(serializers.ModelSerializer):

    class Meta:
        model = Producto
        fields = [
            'id',
            'nombre',
            'precio'
        ]

class CategoriaSimpleSerializer(serializers.ModelSerializer):

    class Meta:
        model = Categoria
        fields = [
            'id',
            'nombre'
        ]

class CategoriaSerializer(serializers.ModelSerializer):

    productos = ProductoSimpleSerializer(
        many=True,
        read_only=True
    )

    class Meta:
        model = Categoria
        fields = [
            'id',
            'nombre',
            'productos'
        ]

class ProductoSerializer(serializers.ModelSerializer):

    categoria = CategoriaSimpleSerializer(
        read_only=True
    )

    categoria_id = serializers.PrimaryKeyRelatedField(
        queryset=Categoria.objects.all(),
        source='categoria',
        write_only=True
    )

    class Meta:
        model = Producto
        fields = [
            'id',
            'nombre',
            'precio',
            'categoria',
            'categoria_id'
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

class CategoriaDetalleSerializer(serializers.ModelSerializer):

    productos = ProductoSimpleSerializer(
        many=True,
        read_only=True
    )

    class Meta:
        model = Categoria
        fields = [
            'id',
            'nombre',
            'productos'
        ]