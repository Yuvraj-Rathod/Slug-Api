from django.contrib import admin
from api.models import Demo_Model

@admin.register(Demo_Model)
class Demo_Admin(admin.ModelAdmin):
    list_display = ['name','id']