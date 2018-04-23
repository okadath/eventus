
from django.conf.urls import url, include
from views import userlogin,LogOut

urlpatterns = [

	url(r'^login/',userlogin,name='login'),
	url(r'^salir/',LogOut,name='logout'),

]

