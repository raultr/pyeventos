from decimal import *
from django.utils import timezone
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
	prioridad = models.DecimalField(default=1.0,max_digits=5,decimal_places=2)
	reporta = models.CharField(max_length=100)
	cdu_estado =models.ForeignKey(CatalogoDetalle,to_field='cdu_catalogo',default='0010000',related_name='evento_cdu_estado',limit_choices_to={'catalogos': 1})
	cdu_municipio= models.ForeignKey(CatalogoDetalle,to_field='cdu_catalogo',default='0020000',related_name='evento_cdu_municipio',limit_choices_to={'catalogos': 2})
	observaciones = models.CharField(max_length=1000 ,blank=True)
	fecha_capturista=models.DateTimeField('fecha_capturista', default=timezone.now)
	fecha_filtro=models.DateTimeField('fecha_filtro', default=timezone.now)
	fecha_evaluador= models.DateTimeField('fecha_evaluador', default=timezone.now)
	revisada = models.BooleanField(default=False)



	def __init__(self, *args, **kwargs):
		super(Evento, self).__init__(*args, **kwargs)
		self.old_fecha_capturista= self.fecha_capturista
		self.old_fecha_filtro= self.fecha_filtro
		self.old_fecha_evaluador= self.fecha_evaluador
		self.old_criticidad_capturista = self.criticidad_capturista

	def mediano(self):
		return Decimal(Decimal(self.criticidad_capturista) /2) + Decimal(Decimal(self.criticidad_evaluador) /2)

	def save(self, *args, **kwargs):	
		#Si alguna tiene un valor anterior que no sea 1900, no se modifica
		
		self.prioridad = Decimal(Decimal(self.criticidad_capturista) /2) + Decimal(Decimal(self.criticidad_evaluador) /2)

		if(self.revisada == True and self.old_criticidad_capturista != self.criticidad_capturista):
			self.criticidad_capturista = self.old_criticidad_capturista
			
		if(self.old_fecha_capturista.year != 1900 and self.revisada == True):
			self.fecha_capturista = self.old_fecha_capturista

		if(self.old_fecha_filtro.year != 1900 and self.fecha_filtro != self.old_fecha_filtro):
			self.fecha_filtro = self.old_fecha_filtro

		if(self.old_fecha_evaluador.year != 1900 and self.fecha_evaluador != self.old_fecha_evaluador ):
			self.fecha_evaluador = self.old_fecha_evaluador


		#Si es una nueva fecha, se pone la fecha del servidor	
		if(self.fecha_capturista.year != 1900 and self.revisada == False):
			self.fecha_capturista =timezone.now()

		if(self.fecha_filtro.year != 1900 and self.old_fecha_filtro.year==1900):
			self.fecha_filtro =timezone.now()
	
		if(self.fecha_evaluador.year != 1900  and self.old_fecha_evaluador.year==1900):
			self.fecha_evaluador =timezone.now()


		super(Evento, self).save(*args, **kwargs)