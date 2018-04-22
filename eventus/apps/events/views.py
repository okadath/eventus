# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render,redirect,get_object_or_404
from models import Event, Category
from forms import EventoForm
from django.core.urlresolvers import reverse
from ..users.models import User



def index(request):
	events=Event.objects.all().order_by('-created')[:6]
	categories=Category.objects.all()

	return render(request, 'index.html',{'events':events,'categories':categories})

def main_panel(request):
	#el '-created' es para ordenar segun fecha de creacion
	events=Event.objects.filter(organizer__username='victorvillazon').order_by('is_free','-created')
	#events=Event.objects.all()
	#organizador=User.objects.get(pk=3)
	#print organizador
	cantidad_eventos=events.count()
	return render(request,'events/panel/panel.html',{'events':events,'cantidad':cantidad_eventos})

def crear_evento(request):
	if request.method=='POST':
		modelform=EventoForm(request.POST,request.FILES)
		if modelform.is_valid():
			organizador=User.objects.get(pk=3)
			print organizador
			nuevo_evento=modelform.save()
			nuevo_evento.organizer=organizador
			nuevo_evento.save()
			#el name space definido y su vsta
			return redirect(reverse('events_app:panel'))
	else:
		modelform=EventoForm()
	return render(request,'events/panel/crear_evento.html',{'form':modelform})

def detalle_evento(request,evento_id):
	event=get_object_or_404(Event,pk=evento_id)
	return render(request,'events/panel/detalle_evento.html',{'event':event})

def editar_evento(request,evento_id):
	event=get_object_or_404(Event,pk=evento_id)
	if request.method=='POST':
		#la instancia es para comparar si ya estaba o es nuevo el cambio
		modelform=EventoForm(request.POST,request.FILES,instance=event)
		if modelform.is_valid():
			modelform.save()
			return redirect(reverse('events_app:panel'))
	#si no fue enviada la peticion rellenar el formulario
	else:
		modelform=EventoForm(instance=event)
#se le pasa eventen el cntexto para que el html lo despliegue
	return render(request,'events/panel/editar_evento.html',{'form':modelform, 'event':event})

def eliminar_evento(request,evento_id):
	event=get_object_or_404(Event,pk=evento_id)
	if request.method=='POST':
		event.delete()
		return redirect(reverse('events_app:panel'))
	return render(request,'events/panel/eliminar_evento.html',{'event':event})


