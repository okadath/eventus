from django import forms
from .models import Event

class EventoForm(forms.ModelForm):
	class Meta:
		model=Event
		#crea los formularios en automatico
		#el exclude evita los atributos que no deben ser generados por
		#el usuario
		exclude=('views','organizer','created','modified',)
		widgets={
		'name':forms.TextInput(attrs={'class':'form-control'}),
		'summary':forms.Textarea(attrs={'class':'form-control','rows':'2'}),
		'content':forms.Textarea(attrs={'class':'form-control','rows':'2'}),
		'category':forms.Select(attrs={'class':'form-control'}),
		'place':forms.TextInput(attrs={'class':'form-control'}),
		'start':forms.DateTimeInput(attrs={'class':'form-control'}),
		'finish':forms.DateTimeInput(attrs={'class':'form-control'}),
		'imagen':forms.ClearableFileInput(attrs={'class':'form-control'}),
		'is_free':forms.CheckboxInput(attrs={'class':'form-control'}),
		'amount':forms.NumberInput(attrs={'class':'form-control'}),
		}
 