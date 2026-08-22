from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from .models import Producto
from .serializers import ProductoSerializer
from django.shortcuts import get_object_or_404


class ProductosView(APIView):

    # GET /api/productos/
    def get(self, request):

        productos = Producto.objects.all()

        serializer = ProductoSerializer(
            productos,
            many=True
        )

        return Response(serializer.data)


    # POST /api/productos/
    def post(self, request):

        serializer = ProductoSerializer(
            data=request.data
        )

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


class ProductoDetalleView(APIView):

    def get_object(self, id):

        return get_object_or_404(
            Producto,
            id=id
        )


    # GET /api/productos/<id>/
    def get(self, request, id):

        producto = self.get_object(id)

        serializer = ProductoSerializer(producto)

        return Response(serializer.data)


    # PUT /api/productos/<id>/
    def put(self, request, id):

        producto = self.get_object(id)

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


    # PATCH /api/productos/<id>/
    def patch(self, request, id):

        producto = self.get_object(id)

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


    # DELETE /api/productos/<id>/
    def delete(self, request, id):

        producto = self.get_object(id)

        producto.delete()

        return Response(
            status=status.HTTP_204_NO_CONTENT
        )