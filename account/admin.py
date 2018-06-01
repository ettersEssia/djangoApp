from django.contrib import admin

# Register your models here.
from .models import pipe, project, parallelepiped

admin.site.register(project)
admin.site.register(parallelepiped)
admin.site.register(pipe)
