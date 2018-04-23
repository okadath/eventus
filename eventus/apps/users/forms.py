from django import forms
from .models import User

class UserRegisterForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ('username','email','password',)
        #son para manejar detalles en templates 
        # con las clases de html form-group
        #el video dice form-control
        widgets={
			'username':forms.TextInput(attrs=
				{
				'class':'form-control',
				'placeholder':'Ingresa nombre'
				}),

			'email':forms.TextInput(attrs=
				{
				'type':'email',
				'class':'form-control',
				'placeholder':'Ingresa mail',
				}),
			'password':forms.TextInput(attrs={
				'type':'password',
				'class':'form-control',
				'placeholder':'Ingresa password',
				}),

        }

class LoginForm(forms.Form):
	#no llama ningun modelo, crea campos por separado
	#por lo tanto no tiene validacion 
	username=forms.CharField(max_length=30,
		widget=forms.TextInput(attrs={
			'class':'form-control',
			'placeholder':'ingresa tu nombre',
			})

		)


	password=forms.CharField(max_length=30,
		widget=forms.TextInput(attrs={
			'type':'password',
			'class':'form-control',
			'placeholder':'ingresa tu password',
			})
		)



