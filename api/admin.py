from django.contrib import admin
from .models import Phone, Rating
from rest_framework.authtoken.admin import TokenAdmin

# Register your models here.
admin.site.register(Phone)
admin.site.register(Rating)
TokenAdmin.raw_id_fields = ['user']