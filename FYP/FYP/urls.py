"""FYP URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.conf.urls import url
from django.contrib import admin
from django.views.generic import TemplateView
from djgeojson.views import GeoJSONLayerView
from safe_road.models import Roads
from safe_road.models import RoadsStop


urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$', TemplateView.as_view(template_name='index.html'), name='home'),
    url(r'^about', TemplateView.as_view(template_name='about.html'), name='about'),
    url(r'^home', TemplateView.as_view(template_name='index.html'),name='home'),
    url(r'^ajax/getStops$', GeoJSONLayerView.as_view(model=RoadsStop, properties='geom, name'), name='Stops'),
    url(r'^ajax/getMain$', GeoJSONLayerView.as_view(model=Roads, properties='geom, name, tweets, collisions, surface'), name='Roads')]
    #url(r'^data.geojson$', GeoJSONLayerView.as_view(model=Location, properties='location, geom, type'),name='data')]
