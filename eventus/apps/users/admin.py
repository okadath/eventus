# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from .models import User

#admin.site.register(User)

# Register your models here.


@admin.register(User)
class UserAdmin(admin.ModelAdmin):
	fieldsets=(
		('User',{'fields':('username','password')}),
		('Personal Info',{'fields':(
			'first_name',
			'last_name',
			'email',
			'avatar',

			)}),
		('Permissions',{'fields':(
			'is_active',
			'is_staff',
			'is_superuser',
			'groups',
			'user_permissions',

			)}),
		)