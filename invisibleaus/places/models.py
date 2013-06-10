from django.db import models

from invisibleaus.generic.models import Place as GenericPlace
from invisibleaus.linkeddata.models import RDFRelationship


class Place(GenericPlace):
    related_places = models.ManyToManyField('places.Place', blank=True, null=True, through='PlaceRelatedPlace')


class PlaceRelatedPlace(models.Model):
    place = models.ForeignKey('places.Place', related_name='main_place')
    related_place = models.ForeignKey('places.Place', related_name='related_place')
    relationship = models.ForeignKey('places.PlaceRelationship')


class PlaceRelationship(RDFRelationship):
    ''' Relationship between places -- eg suburb -> city, city -> country '''
