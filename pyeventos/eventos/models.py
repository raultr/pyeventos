from decimal import *
from django.core.files import File
import urllib
from django.db import models
from catalogos_detalle.models import CatalogoDetalle
from django.core.validators import RegexValidator
from django.core.exceptions import ValidationError
from django.core.validators import MinValueValidator, MaxValueValidator


class Evento(models.Model):
	descripcion = models.CharField(max_length=1000)
	cdu_fuente = models.ForeignKey(CatalogoDetalle,to_field='cdu_catalogo',default='0030000',related_name='evento_cdu_fuente',limit_choices_to={'catalogos': 3})		
	criticidad_capturista = models.IntegerField(default=1,validators=[MinValueValidator(1),MaxValueValidator(7)])
	criticidad_evaluador = models.IntegerField(default=1,validators=[MinValueValidator(1),MaxValueValidator(7)])
	reporta = models.CharField(max_length=100)
	cdu_estado =models.ForeignKey(CatalogoDetalle,to_field='cdu_catalogo',default='0010000',related_name='evento_cdu_estado',limit_choices_to={'catalogos': 1})
	cdu_municipio= models.ForeignKey(CatalogoDetalle,to_field='cdu_catalogo',default='0020000',related_name='evento_cdu_municipio',limit_choices_to={'catalogos': 2})
	observaciones = models.CharField(max_length=1000 ,blank=True)
	fecha_capturista=models.DateField(default = '1900-01-01')
	fecha_filtro=models.DateField(    default = '1900-01-01')
	fecha_evaluador=models.DateField( default = '1900-01-01')
	revisada = models.BooleanField(default=False)

	def mediano(self):
		return Decimal(Decimal(self.criticidad_capturista) /2) + Decimal(Decimal(self.criticidad_evaluador) /2)