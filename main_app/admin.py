from django.contrib import admin
from .models import Trip, Stop, Photo

# Register your models here.
admin.site.register(Trip)
admin.site.register(Stop)
admin.site.register(Photo)