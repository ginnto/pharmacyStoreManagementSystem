from django.contrib import admin
from . models import *
# Register your models here.
class med(admin.ModelAdmin):
    list_display = ['name','slug']
   
admin.site.register(Medicine,med)


class cat(admin.ModelAdmin):
    list_display = ['name','slug']

admin.site.register(category,cat)