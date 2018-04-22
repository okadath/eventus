# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render,redirect,get_object_or_404
from models import Event, Category
from forms import EventoForm
from django.core.urlresolvers import reverse,reverse_lazy
from ..users.models import User
from django.views.generic import TemplateView,CreateView,DetailView,UpdateView,DeleteView

def login(request):
	return render(request,"login.html",{})

class IndexView(TemplateView):
	template_name='index.html'

	def get_context_data(self, **kwargs):
	    context = super(IndexView, self).get_context_data(**kwargs)
	    #obtiene las variables(contexto) para desplegar
	    context['events']=Event.objects.all().order_by('-created')[:6]
	    context['categories']=Category.objects.all()

	    return context


class MainPanelView(TemplateView):
	template_name='events/panel/panel.html'

	def get_context_data(self, **kwargs):
	    context = super(MainPanelView, self).get_context_data(**kwargs)
	    context['events']=Event.objects.filter(organizer__username='victorvillazon').order_by('is_free','-created')
	    context['cantidad']=context['events'].count()
	   	#hay diferencia ()?? si
	    return context		

# def main_panel(request):
# 	#el '-created' es para ordenar segun fecha de creacion
# 	events=Event.objects.filter(organizer__username='victorvillazon').order_by('is_free','-created')
# 	cantidad_eventos=events.count()
# 	return render(request,'events/panel/panel.html',{'events':events,'cantidad':cantidad_eventos})


class CreateEvent(CreateView):
	form_class=EventoForm
	template_name='events/panel/crear_evento.html'
	#reverse abre otra pagina en automatico
	#para evitar eso usamos reverse lazy
	success_url=reverse_lazy('events_app:panel')

	def form_valid(self,form):
		print 'es valido'
		#usar un request para usar el logeado, mientras esto :v
		form.instance.organizer=User.objects.get(pk=1)
		return super(CreateEvent,self).form_valid(form)

# def crear_evento(request):
# 	if request.method=='POST':
# 		modelform=EventoForm(request.POST,request.FILES)
# 		if modelform.is_valid():
# 			organizador=User.objects.get(pk=3)
# 			print organizador
# 			nuevo_evento=modelform.save()
# 			nuevo_evento.organizer=organizador
# 			nuevo_evento.save()
# 			#el name space definido y su vsta
# 			return redirect(reverse('events_app:panel'))
# 	else:
# 		modelform=EventoForm()
# 	return render(request,'events/panel/crear_evento.html',{'form':modelform})


class EventDetail(DetailView):
	template_name='events/panel/detalle_evento.html'
	#creo que lo lee asi por sus huevos :v
	model=Event
# def detalle_evento(request,evento_id):
# 	event=get_object_or_404(Event,pk=evento_id)
# 	return render(request,'events/panel/detalle_evento.html',{'event':event})



class EventEdit(UpdateView):
	#me parece que las views manejan el model en automatico cn 
	#las solicitudes a la bd y al modelo
    model = Event
    form_class=EventoForm

    template_name = 'events/panel/editar_evento.html'
    success_url=reverse_lazy('events_app:panel')

    #para la edicion el mismo problema del usuario
    def form_valid(self,form):
    	form.instance.organizer=User.objects.get(pk=3)
    	return super(EventEdit,self).form_valid(form)
# def editar_evento(request,evento_id):
# 	event=get_object_or_404(Event,pk=evento_id)
# 	if request.method=='POST':
# 		#la instancia es para comparar si ya estaba o es nuevo el cambio
# 		modelform=EventoForm(request.POST,request.FILES,instance=event)
# 		if modelform.is_valid():
# 			modelform.save()
# 			return redirect(reverse('events_app:panel'))
# 	#si no fue enviada la peticion rellenar el formulario
# 	else:
# 		modelform=EventoForm(instance=event)
# #se le pasa eventen el cntexto para que el html lo despliegue
# 	return render(request,'events/panel/editar_evento.html',{'form':modelform, 'event':event})

class EventDelete(DeleteView):
 	model = Event
	template_name = 'events/panel/eliminar_evento.html'
	success_url=reverse_lazy('events_app:panel')
	#evento a eliminar
	context_object_name='event'


# def eliminar_evento(request,evento_id):
# 	event=get_object_or_404(Event,pk=evento_id)
# 	if request.method=='POST':
# 		event.delete()
# 		return redirect(reverse('events_app:panel'))
# 	return render(request,'events/panel/eliminar_evento.html',{'event':event})


