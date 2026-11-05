from django.contrib import admin
from myapp.models import student

# Register your models here.
class studentadmin(admin.ModelAdmin):
    list_display=['name','place','email']
admin.site.register(student,studentadmin)


