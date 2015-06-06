from rest_framework import serializers
from catalogos_detalle.serializers import CatalogoSerializer
from catalogos_detalle.models import CatalogoDetalle

from .models import Evento



class EventoSerializer(serializers.ModelSerializer):
	fecha_capturista = serializers.DateTimeField(format='%d/%m/%Y',input_formats=['%d/%m/%Y'])
	fecha_filtro =serializers.DateTimeField(format='%d/%m/%Y',input_formats=['%d/%m/%Y'])
	fecha_evaluador =serializers.DateTimeField(format='%d/%m/%Y',input_formats=['%d/%m/%Y'])

	class Meta:
		model = Evento

		fields=('id','descripcion','cdu_fuente','criticidad_capturista','criticidad_evaluador','reporta','cdu_estado',
		'cdu_municipio','observaciones','fecha_capturista','fecha_filtro','fecha_evaluador','revisada')

# class EventoSerializerRelacion(serializers.ModelSerializer):
# 	fecha_capturista = serializers.DateTimeField(format='%d/%m/%Y',input_formats=['%d/%m/%Y'])
# 	fecha_filtro =serializers.DateTimeField(format='%d/%m/%Y',input_formats=['%d/%m/%Y'])
# 	fecha_evaluador =serializers.DateTimeField(format='%d/%m/%Y',input_formats=['%d/%m/%Y'])
# 	cdu_fuente = CatalogoSerializer(read_only=True, required=False,many=True)
# 	cdu_estado = CatalogoSerializer(read_only=True, required=False,many=True)
# 	cdu_municipio = CatalogoSerializer(read_only=True, required=False,many=True)
# 	cdu_fuente_id = serializers.PrimaryKeyRelatedField(write_only=True,  source='cdu_fuente')
# 	cdu_estado_id = serializers.PrimaryKeyRelatedField(write_only=True,  source='cdu_estado')
# 	cdu_municipio_id = serializers.PrimaryKeyRelatedField(write_only=True,  source='cdu_municipio')

# 	class Meta:
# 		model = Evento
# 		fields=('id','descripcion','cdu_fuente','criticidad_capturista','criticidad_evaluador','reporta','cdu_estado',
# 		'cdu_municipio','observaciones','fecha_capturista','fecha_filtro','fecha_evaluador','revisada',)