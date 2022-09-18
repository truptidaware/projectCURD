from django.contrib import admin
from .models import prod
# Register your models here.


class prodAdmin(admin.ModelAdmin):
    list_display = ['id','name','rate']

admin.site.register(prod,prodAdmin)
