from rest_framework import serializers
from .models import Evento


class EventoSerializer(serializers.ModelSerializer):
	fecha_capturista = serializers.DateTimeField(format='%d/%m/%Y',input_formats=['%d/%m/%Y'])
	fecha_filtro =serializers.DateTimeField(format='%d/%m/%Y',input_formats=['%d/%m/%Y'])
	fecha_evaluador =serializers.DateTimeField(format='%d/%m/%Y',input_formats=['%d/%m/%Y'])

	class Meta:
		model = Evento

		fields=('id','descripcion','cdu_fuente','criticidad_capturista','criticidad_evaluador','reporta','cdu_estado',
		'cdu_municipio','observaciones','fecha_capturista','fecha_filtro','fecha_evaluador','revisada')