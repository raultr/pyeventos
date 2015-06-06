from django.contrib import admin
from .models import Evento

class EventoAdmin(admin.ModelAdmin):
	list_display =('id','revisada','descripcion','criticidad_capturista','cdu_fuente','cdu_estado','cdu_municipio','criticidad_evaluador','mediano','reporta','fecha_capturista','fecha_filtro','fecha_evaluador','observaciones')
	list_filter =('cdu_estado','cdu_fuente','criticidad_capturista','criticidad_evaluador','revisada')
	search_fields = ('descripcion','fecha_capturista') # Campos por los que se puede buscar, si son campos foraneos se usa campo__nomcampoforaneo
	list_editable=('revisada','criticidad_capturista','criticidad_evaluador')
	#list_editable = ('catalogos','descripcion1','descripcion2','monto1','monto2','cdu_default') # Hace el campo editable, (no debe ser el primer campo del list_display)
	#raw_id_fields = ('catalogos',) # Para que me muestre solo el id y si queremos buscarlo por nombre nos pone una lupita
	
			
admin.site.register(Evento,EventoAdmin)


