from django.shortcuts import render, get_object_or_404, get_list_or_404
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.parsers import JSONParser
from rest_framework.parsers import FileUploadParser
from .serializers import CatalogoSerializer
from .models import CatalogoDetalle
	

	
@api_view(['GET', 'POST'])
def request_response_list(request,id_catalogo):
	if request.method == 'GET':
		catalogo_detalle= get_list_or_404(CatalogoDetalle, catalogos=id_catalogo)
		serializer = CatalogoSerializer(catalogo_detalle, many=True)
		return Response(serializer.data)

@api_view(['GET'])
def request_response_detalle(request,id_catalogo):
	if request.method == 'GET':
		listado = id_catalogo.split(',')
		catalogo_detalle=CatalogoDetalle.objects.filter(catalogos__in=listado).order_by('catalogos', 'descripcion1')
		serializer = CatalogoSerializer(catalogo_detalle, many=True)
		return Response(serializer.data)


@api_view(['GET'])
def request_response_detalle_cdu_default(request,id_catalogo,cdu_default):
	if request.method == 'GET':
		listado = id_catalogo.split(',')
		catalogo_detalle=CatalogoDetalle.objects.filter(catalogos__in=listado,cdu_default=cdu_default).order_by('catalogos', 'descripcion1')
		serializer = CatalogoSerializer(catalogo_detalle, many=True)
		return Response(serializer.data)



@api_view(['POST'])
def request_response_nuevo(request):
	if request.method == 'POST':
		serializer = CatalogoSerializer(data=request.DATA)

		if serializer.is_valid():
			serializer.save()
			return Response(serializer.data, status=status.HTTP_201_CREATED)
		return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)