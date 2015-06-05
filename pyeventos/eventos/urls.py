from django.conf.urls import patterns, url
from rest_framework.urlpatterns import format_suffix_patterns
from eventos import views

urlpatterns = patterns('eventos.views',
	 url(r'^eventos/(?P<pk>[0-9]+)/$',views.EventoOperaciones.as_view(), name='evento_por_pk'),
	 url(r'^eventos/$',views.EventoOperaciones.as_view(), name='evento_todos'),	   
	  url(r'^eventos/revisado/$',views.EventosRevisados.as_view(), name='evento_buscar'),	   
	 url(r'^eventos/norevisado/$',views.EventosNoRevisados.as_view(), name='evento_buscar'),	   
	
	)