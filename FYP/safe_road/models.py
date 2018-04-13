from django.db import models

# Create your models here.
from django.contrib.gis.db import models

class Location(models.Model):
    # using django fields to represent database
    location = models.CharField(max_length=100)
    geom = models.PointField()

    def _str_(self):
        return self.location

class Roads(models.Model):
    location_id = models.IntegerField(primary_key=True)
    geom = models.GeometryField(blank=True, null=True)
    name = models.CharField(max_length=100, blank=True, null=True)
    id = models.CharField(max_length=100, blank=True, null=True)
    alt_name = models.CharField(max_length=100, blank=True, null=True)
    bicycle = models.CharField(max_length=100, blank=True, null=True)
    highway = models.CharField(max_length=100, blank=True, null=True)
    surface = models.CharField(max_length=100, blank=True, null=True)
    lit = models.CharField(max_length=100, blank=True, null=True)
    access = models.CharField(max_length=100, blank=True, null=True)
    maxspeed = models.CharField(max_length=100, blank=True, null=True)
    maxheight = models.CharField(max_length=100, blank=True, null=True)
    oneway = models.CharField(max_length=100, blank=True, null=True)
    width = models.CharField(max_length=100, blank=True, null=True)
    maxweight = models.CharField(max_length=100, blank=True, null=True)
    maxwidth = models.CharField(max_length=100, blank=True, null=True)
    collisions = models.IntegerField(blank=True, null=True)
    tweets = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'map_data'

class RoadsStop(models.Model):
    location_id = models.IntegerField(primary_key=True)
    geom = models.GeometryField(blank=True, null=True)
    name = models.CharField(max_length=100, blank=True, null=True)
    type = models.CharField(max_length=100, blank=True, null=True)
    id = models.CharField(max_length=100, blank=True, null=True)
    alt_name = models.CharField(max_length=100, blank=True, null=True)
    bicycle = models.CharField(max_length=100, blank=True, null=True)
    highway = models.CharField(max_length=100, blank=True, null=True)
    surface = models.CharField(max_length=100, blank=True, null=True)
    lit = models.CharField(max_length=100, blank=True, null=True)
    access = models.CharField(max_length=100, blank=True, null=True)
    maxspeed = models.CharField(max_length=100, blank=True, null=True)
    maxheight = models.CharField(max_length=100, blank=True, null=True)
    oneway = models.CharField(max_length=100, blank=True, null=True)
    width = models.CharField(max_length=100, blank=True, null=True)
    maxweight = models.CharField(max_length=100, blank=True, null=True)
    maxwidth = models.CharField(max_length=100, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'roads_stop'