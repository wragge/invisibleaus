from django.db import models
from invisibleaus.linkeddata.models import RDFRelationship, RDFType
from invisibleaus.generic.models import Event, Period, Person, Group, StandardMetadata
from invisibleaus.events.models import SeaVoyage, TravelEvent

# Create your models here.


class StandardSources(models.Model):
    records = models.ManyToManyField(
                        'sources.Record',
                        blank=True,
                        null=True
                        )
    photographs = models.ManyToManyField(
                            'sources.Photograph',
                            blank=True,
                            null=True
                            )
    publications = models.ManyToManyField(
                            'sources.Publication',
                            blank=True,
                            null=True
                            )

    class Meta:
        abstract = True


class PersonPlaces(models.Model):
    birth_place = models.ForeignKey(
                            'places.Place',
                            blank=True,
                            null=True,
                            related_name='%(app_label)s_%(class)s_birth_place'
                            )
    death_place = models.ForeignKey(
                            'places.Place',
                            blank=True,
                            null=True,
                            related_name='%(app_label)s_%(class)s_death_place'
                            )

    class Meta:
        abstract = True


class Resident(Person, PersonPlaces):
    '''Australian resident subject to WAP.'''
    related_people = models.ManyToManyField(
                                'people.Resident',
                                blank=True,
                                null=True,
                                through='ResidentRelatedResident'
                                )
    papertrails = models.BooleanField(default=False)  # Part of Paper trails dataset.


class Official(Person, PersonPlaces):
    '''Government official'''


class Identity(models.Model):
    '''Person recorded in specific life event.'''
    display_name = models.CharField(max_length=200)
    resident = models.ForeignKey('people.Resident', blank=True, null=True)


class NamePart(models.Model):
    '''Part of a name.'''
    part = models.CharField(max_length=100)
    name_type = models.ForeignKey('people.NameType')
    identity = models.ForeignKey('people.Identity')


class Family(Group):
    members = models.ManyToManyField('people.Resident')


class SeaVoyageGroup(Group):
    members = models.ManyToManyField('people.Resident')
    sea_voyage = models.ForeignKey('events.SeaVoyage', blank=True, null=True)


class Repository(Group):
    ''' Organisation that holds records. '''


class Agency(Group):
    ''' Government organisation that creates records. '''


class LifeEvent(Event, StandardSources):
    '''Event in the life of a person.'''
    identity = models.ForeignKey('people.Identity')
    life_event_type = models.ForeignKey('people.LifeEventType')
    related_identities = models.ManyToManyField('people.Identity', blank=True, null=True, through='LifeEventIdentity', related_name='related_identities')


class LifePeriod(Period, StandardSources):
    '''Defined period in a person's life, eg: marriage, residence, employment.'''
    identity = models.ForeignKey('people.Identity')
    related_life_event = models.ManyToManyField('people.LifeEvent', blank=True, null=True, through='people.LifePeriodEvent')
    life_period_type = models.ForeignKey('people.LifePeriodType')


class ResidentRelatedResident(models.Model):
    resident = models.ForeignKey('people.Resident', related_name='main_resident')
    related_resident = models.ForeignKey('people.Resident', related_name='related_resident')
    relationship = models.ForeignKey('people.ResidentRelationship')


class LifeEventIdentity(models.Model):
    life_event = models.ForeignKey('people.LifeEvent')
    identity = models.ForeignKey('people.Identity')
    relationship = models.ForeignKey('people.LifeEventIdentityRelationship')


class LifePeriodEvent(models.Model):
    life_event = models.ForeignKey('people.LifeEvent')
    life_period = models.ForeignKey('people.LifePeriod')
    relationship = models.ForeignKey('people.LifePeriodEventRelationship')


class NameType(RDFType):
    '''Type of name, eg: family.'''


class LifeEventType(RDFType):
    '''Type of life event, eg: birth.'''


class LifePeriodType(RDFType):
    '''Type of life period, eg: marriage.'''


class ResidentRelationship(RDFRelationship):
    '''Relationship between people, eg: mother - child.'''


class LifePeriodEventRelationship(RDFRelationship):
    '''Relationship between a life period and an associated life event, eg: start.'''


class LifeEventIdentityRelationship(RDFRelationship):
    '''Relationship between life event and other people (not the subject).'''


