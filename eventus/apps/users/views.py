# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render,redirect
from .forms import UserRegisterForm,LoginForm
from .models import User
from django.utils import timezone
from django.contrib.auth import login,authenticate,logout

# Create your views here.

#esto es para enviar el formulario
#{{ user_register.username }}
#{{ user_register.username.errors }} del template
def userlogin(request):
	#si ya enviamos el formulario:
	if request.method=='POST':
		#si hay una variable en el HTML llamada register form
		#el nombre de la etiqueta html
		if 'register_form' in request.POST:
			user_register=UserRegisterForm(request.POST)
			if user_register.is_valid():
				User.objects.create_user(username=user_register.cleaned_data['username'],
					email=user_register.cleaned_data['email'],password=user_register.cleaned_data['password'],
					last_login=timezone.now() )
				return redirect('/')
		if 'login_form' in request.POST:
			login_form=LoginForm(request.POST)
			if login_form.is_valid():
				#authenticate devuelve el objeto del usuario o none
				user=authenticate(username=login_form.cleaned_data['username'],
					password=login_form.cleaned_data['password'])
				if user is not None:
					if user.is_active:
						login(request,user)
						return redirect('/')


	#si aun no enviamos el form de signin:
	else:
		user_register=UserRegisterForm()
		login_form=LoginForm()

		#el contexto envia la info de los formularios
	return render(request,'users/login.html',
		{'user_register':user_register,'login_form':login_form,})

def LogOut(request):
	logout(request)
	return redirect('/')
