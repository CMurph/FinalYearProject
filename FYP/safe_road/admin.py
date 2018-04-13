from django.contrib import admin

# Register your models here.
from django.contrib.gis import admin
from .models import Location

admin.site.register(Location, admin.GeoModelAdmin)
