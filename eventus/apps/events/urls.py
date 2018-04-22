
from django.conf.urls import url, include
from django.contrib import admin
from views import index, main_panel,crear_evento,detalle_evento,editar_evento,eliminar_evento


urlpatterns = [
	url(r'^$',index, name= 'index'),
	url(r'^index',index, name= 'index'),
	url(r'^panel/$',main_panel, name= 'panel'),
	url(r'^panel/evento/nuevo/$',crear_evento, name= 'nuevo'),
	url(r'^panel/evento/(?P<evento_id>\d+)/$',detalle_evento, name= 'detalle'),
	url(r'^panel/evento/editar/(?P<evento_id>\d+)/$',editar_evento, name= 'editar'),
	url(r'^panel/evento/eliminar/(?P<evento_id>\d+)/$',eliminar_evento, name= 'eliminar'),

]

