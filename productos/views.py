from django.shortcuts import render

from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status

from .models import Producto
from .serializers import ProductoSerializer


# GET: Obtener todos los productos
# POST: Crear un producto
@api_view(['GET', 'POST'])
def productos(request):

    # Obtener todos los productos
    if request.method == 'GET':

        productos = Producto.objects.all()

        serializer = ProductoSerializer(productos, many=True)

        return Response(serializer.data)


    # Crear un producto
    elif request.method == 'POST':

        serializer = ProductoSerializer(data=request.data)

        if serializer.is_valid():

            serializer.save()

            return Response(
                serializer.data,
                status=status.HTTP_201_CREATED
            )

        return Response(
            serializer.errors,
            status=status.HTTP_400_BAD_REQUEST
        )


# GET: Obtener un producto
# PUT: Actualizar un producto
# DELETE: Eliminar un producto
@api_view(['GET', 'PUT', 'PATCH', 'DELETE'])
def producto_detalle(request, id):

    try:
        producto = Producto.objects.get(id=id)

    except Producto.DoesNotExist:

        return Response(
            {"error": "Producto no encontrado"},
            status=status.HTTP_404_NOT_FOUND
        )


    # GET: Obtener un producto
    if request.method == 'GET':

        serializer = ProductoSerializer(producto)

        return Response(serializer.data)


    # PUT: Actualizar completamente
    elif request.method == 'PUT':

        serializer = ProductoSerializer(
            producto,
            data=request.data
        )

        if serializer.is_valid():

            serializer.save()

            return Response(serializer.data)

        return Response(
            serializer.errors,
            status=status.HTTP_400_BAD_REQUEST
        )


    # PATCH: Actualizar parcialmente
    elif request.method == 'PATCH':

        serializer = ProductoSerializer(
            producto,
            data=request.data,
            partial=True
        )

        if serializer.is_valid():

            serializer.save()

            return Response(serializer.data)

        return Response(
            serializer.errors,
            status=status.HTTP_400_BAD_REQUEST
        )


    # DELETE: Eliminar un producto
    elif request.method == 'DELETE':

        producto.delete()

        return Response(
            status=status.HTTP_204_NO_CONTENT
        )