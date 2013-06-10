from django.db import models
from django.core.urlresolvers import reverse

from invisibleaus.linkeddata.models import RDFRelationship, RDFType
from invisibleaus.generic.models import Event, Period, Person, Group, StandardMetadata, URI


# Create your models here.


class RecordURI(URI):
    record = models.ForeignKey('sources.Record')


class RecordSource(StandardMetadata):
    identifier = models.CharField(max_length=100, blank=True, null=True)  # Alphanumeric repository id eg MS129, A1, 1957/1234
    numeric_identifier = models.IntegerField(blank=True, null=True)  # Barcode or other unique numeric id
    title = models.TextField(blank=True, null=True)
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


class ItemsManager(models.Manager):
    def get_query_set(self):
        return super(ItemsManager, self).get_query_set().filter(record_type__label='item')


class SeriesManager(models.Manager):
    def get_query_set(self):
        return super(SeriesManager, self).get_query_set().filter(record_type__label='series')


class DocManager(models.Manager):
    def get_query_set(self):
        return super(DocManager, self).get_query_set().filter(record_type__label='document')


class Record(RecordSource):
    '''An individual record or document held within an archive.'''
    is_part_of = models.ForeignKey('sources.Record', blank=True, null=True, related_name='part_of')
    record_type = models.ForeignKey('sources.RecordType', blank=True, null=True)
    number_of_items = models.IntegerField(blank=True, null=True)
    repository = models.ForeignKey('people.Repository', blank=True, null=True)
    related_records = models.ManyToManyField('sources.Record', blank=True, null=True, through='RecordRelatedRecord')
    access_status = models.CharField(max_length=30, blank=True, null=True)
    long_citation = models.TextField(blank=True, null=True)
    short_citation = models.CharField(max_length=100, blank=True, null=True)
    start_page = models.IntegerField(blank=True, null=True)
    end_page = models.IntegerField(blank=True, null=True)

    objects = models.Manager()
    items = ItemsManager()
    series = SeriesManager()
    docs = DocManager()

    def __unicode__(self):
        return '{}: {}, {}'.format(self.repository, self.short_citation, self.title)

    def get_absolute_url(self):
        return reverse('record-view', kwargs={'id': self.id})


class RecordRelatedRecord(models.Model):
    record = models.ForeignKey('sources.Record', related_name='main_record')
    related_record = models.ForeignKey('sources.Record', related_name='related_record')
    relationship = models.ForeignKey('sources.RecordRelationship')


class RecordType(RDFType):
    '''Type of record, eg: series, file, document.'''


class RecordRelationship(RDFRelationship):
    '''Related aggregations, eg: succeeding series, controlling series'''


class RecordStats(StandardMetadata):
    record = models.ForeignKey('sources.Record')
    # Number of items in this aggregation described in system
    number_described = models.IntegerField(blank=True, null=True)
    number_described_note = models.TextField(blank=True)
    # Number of items in this aggregation currently digitised
    number_digitised = models.IntegerField(blank=True, null=True)
    linear_size = models.DecimalField(max_digits=8, decimal_places=3, blank=True, null=True)


class NSWBDMRecord(Record):
    registration_year = models.IntegerField(blank=True, null=True)
    registration_number = models.IntegerField(blank=True, null=True)
    registration_place = models.ForeignKey('places.Place', null=True, blank=True)
    volume_reference = models.CharField(max_length=20, blank=True, null=True)


class Photograph(models.Model):
    '''A photograph.'''


class Publication(models.Model):
    '''A published source.'''



