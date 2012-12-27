from django.db import models
from invisibleaus.linkeddata.models import RDFRelationship, RDFType
from invisibleaus.generic.models import Event, Period, Person, StandardMetadata

# Create your models here.


class TravelEvent(Event):
    start_place = models.ForeignKey(
                        'places.Place',
                        blank=True,
                        null=True,
                        related_name='%(app_label)s_%(class)s_start_place'
                        )
    end_place = models.ForeignKey(
                        'places.Place',
                        blank=True,
                        null=True,
                        related_name='%(app_label)s_%(class)s_end_place'
                        )

    class Meta:
        abstract = True


class SeaVoyage(Period):
    embarkation_place = models.ForeignKey(
                                'places.Place',
                                related_name='embarkation_place'
                                )
    destination_place = models.ForeignKey(
                                'places.Place',
                                related_name='destination_place'
                                )
    ship = models.ForeignKey('things.Ship')


class SeaVoyageLeg(TravelEvent):
    '''Part of a sea voyage between ports.'''
    sea_voyage = models.ForeignKey('events.SeaVoyage')

