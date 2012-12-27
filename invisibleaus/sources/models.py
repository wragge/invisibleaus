from django.db import models
from invisibleaus.linkeddata.models import RDFRelationship, RDFType
from invisibleaus.generic.models import Event, Period, Person, Group, StandardMetadata, URI


# Create your models here.


class RecordAggregationURI(URI):
    aggregation = models.ForeignKey('sources.RecordAggregation')


class RecordURI(URI):
    record = models.ForeignKey('sources.Record')


class RecordSource(StandardMetadata):
    identifier = models.CharField(max_length=100)  # Alphanumeric repository id eg MS129, A1, 1957/1234
    numeric_identifier = models.IntegerField(blank=True, null=True)  # Barcode or other unique numeric id
    title = models.TextField()
    date_string = models.CharField(max_length=50, blank=True)  # Original text representation of dates
    start_date = models.DateField(null=True, blank=True)
    start_month_known = models.BooleanField(default=False)
    start_day_known = models.BooleanField(default=False)
    end_date = models.DateField(null=True, blank=True)
    end_month_known = models.BooleanField(default=False)
    end_day_known = models.BooleanField(default=False)
    description = models.TextField(blank=True)

    class Meta:
        abstract = True


class RecordAggregation(RecordSource):
    '''Some sort of aggregation of records, eg collection, series, file, box.'''
    aggregation_type = models.ForeignKey('sources.AggregationType')
    number_of_items = models.IntegerField(blank=True, null=True)
    linear_size = models.DecimalField(max_digits=8, decimal_places=3, blank=True, null=True)
    repository = models.ForeignKey('people.Repository', blank=True, null=True)
    agencies = models.ManyToManyField('people.Agency', blank=True, null=True, through='AggregationRelatedAgency')
    related_aggregations = models.ManyToManyField('sources.RecordAggregation', blank=True, null=True, through='AggregationRelatedAggregation')


class AggregationRelatedAggregation(models.Model):
    aggregation = models.ForeignKey('sources.RecordAggregation', related_name='main_aggregation')
    related_aggregation = models.ForeignKey('sources.RecordAggregation', related_name='related_aggregation')
    relationship = models.ForeignKey('sources.AggregationRelationship')


class AggregationType(RDFType):
    '''Type of aggregation, eg: series, file.'''


class AggregationRelationship(RDFRelationship):
    '''Related aggregations, eg: succeeding series, file is a part of a series.'''


class AggregationStats(StandardMetadata):
    aggregation = models.ForeignKey('sources.RecordAggregation')
    # Number of items in this aggregation described in system
    number_described = models.IntegerField(max_length=8, blank=True, null=True)
    number_described_note = models.TextField(blank=True)
    # Number of items in this aggregation currently digitised
    number_digitised = models.IntegerField(max_length=8, blank=True, null=True)
    # Total number of digitised images from this aggregation
    number_digitised_pages = models.IntegerField(blank=True, null=True)


class AggregationRelatedAgency(models.Model):
    aggregation = models.ForeignKey('sources.RecordAggregation')
    agency = models.ForeignKey('people.Agency')
    relationship = models.ForeignKey('sources.AggregationAgencyRelationship')


class AggregationAgencyRelationship(RDFRelationship):
    ''' Eg. Creating, controlling. '''


class Record(RecordSource):
    '''An individual record or document held within an archive.'''
    aggregation = models.ForeignKey('sources.RecordAggregation', blank=True, null=True)
    related_officials = models.ManyToManyField(
                                    'people.Official', through='RecordRelatedOfficial'
                                )
    related_residents = models.ManyToManyField(
                                    'people.Resident', through='RecordRelatedResident'
                                )


class NSWBDMRecord(Record):
    registration_year = models.IntegerField(blank=True, null=True)
    registration_number = models.IntegerField(blank=True, null=True)
    registration_place = models.ForeignKey('places.Place', null=True, blank=True)
    volume_reference = models.CharField(max_length=20, blank=True, null=True)


class RecordRelatedResident(models.Model):
    record = models.ForeignKey('sources.Record')
    resident = models.ForeignKey('people.Resident')
    relationship = models.ForeignKey('sources.RecordPersonRelationship')


class RecordRelatedOfficial(models.Model):
    record = models.ForeignKey('sources.Record')
    resident = models.ForeignKey('people.Official')
    relationship = models.ForeignKey('sources.RecordPersonRelationship')


class RecordPersonRelationship(RDFRelationship):
    ''' Eg: author, recipient, subject. '''


class Photograph(models.Model):
    '''A photograph.'''


class Publication(models.Model):
    '''A published source.'''



