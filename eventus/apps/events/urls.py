
from django.conf.urls import url, include
from django.contrib import admin
from views import IndexView,MainPanelView,CreateEvent,EventDetail,EventEdit,EventDelete

#index, main_panel,crear_evento,detalle_evento,editar_evento,eliminar_evento


urlpatterns = [
	#vistas basadas en clases
	url(r'^$',IndexView.as_view(), name= 'index'),
	#url(r'^login/$',login,name='login'),
	url(r'^panel/$',MainPanelView.as_view(), name= 'panel'),
	url(r'^panel/evento/nuevo/$',CreateEvent.as_view(), name= 'nuevo'),
	url(r'^panel/evento/(?P<pk>\d+)/$',EventDetail.as_view(), name= 'detalle'),
 	url(r'^panel/evento/editar/(?P<pk>\d+)/$',EventEdit.as_view(), name= 'editar'),
	url(r'^panel/evento/eliminar/(?P<pk>\d+)/$',EventDelete.as_view(), name= 'eliminar'),
]

