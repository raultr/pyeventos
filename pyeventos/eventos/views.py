import re
from django.shortcuts import render, get_object_or_404, get_list_or_404 
from django.http import Http404
from django.db import connection
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.parsers import JSONParser
from .serializers import EventoSerializer
from rest_framework.views import APIView
from rest_framework.generics import CreateAPIView
from rest_framework import parsers
from .models import Evento
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from rest_framework.pagination import PageNumberPagination

class EventoOperaciones(APIView):	

	def get_object(self, pk):
		try:
			return Evento.objects.get(pk=pk)
		except Evento.DoesNotExist:
			raise Http404

	def get(self, request, pk=None, format=None):
		if(pk!=None):
			evento = self.get_object(pk)
			serializer = EventoSerializer(evento)
			return Response(serializer.data)
		evento = Evento.objects.all()
		serializer = EventoSerializer(evento, many=True)
		pagination_class = LargeResultsSetPagination
		return Response(serializer.data)
	
	def post(self, request):
		serializer = EventoSerializer(data=request.DATA)
		if serializer.is_valid():
			serializer.save()
			return Response(serializer.data, status=status.HTTP_201_CREATED)
		return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
 
	def put(self, request, pk, format=None):
		id = self.get_object(pk)
		serializer = EventoSerializer(id,data=request.DATA)
		print "Estoy validando"
		if serializer.is_valid():
			print "ya valide"
			serializer.save()
			return Response(serializer.data, status=status.HTTP_201_CREATED)
		return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class LargeResultsSetPagination(PageNumberPagination):
    page_size = 1000
    page_size_query_param = 'page_size'
    max_page_size = 10000