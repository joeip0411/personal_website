from django.contrib import admin

# Register your models here.
from .models import Project

class PostProject(admin.ModelAdmin):
    pass


admin.site.register(Project, PostProject)
