from django.db import models

# Create your models here.


class StandardMetadata(models.Model):
    date_created = models.DateTimeField(auto_now_add=True)
    date_modified = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True


class Thing(StandardMetadata):
    label = models.CharField(max_length=250, blank=True, null=True)
    description = models.TextField(blank=True, null=True)

    class Meta:
        abstract = True

    def __unicode__(self):
        return self.label


class Person(StandardMetadata):
    display_name = models.CharField(max_length=200)
    biography = models.TextField(blank=True, null=True)
    birth_earliest_date = models.DateField(null=True, blank=True)
    birth_earliest_month_known = models.BooleanField(default=False)
    birth_earliest_day_known = models.BooleanField(default=False)
    birth_latest_date = models.DateField(null=True, blank=True)
    birth_latest_month_known = models.BooleanField(default=False)
    birth_latest_day_known = models.BooleanField(default=False)
    death_earliest_date = models.DateField(null=True, blank=True)
    death_earliest_month_known = models.BooleanField(default=False)
    death_earliest_day_known = models.BooleanField(default=False)
    death_latest_date = models.DateField(null=True, blank=True)
    death_latest_month_known = models.BooleanField(default=False)
    death_latest_day_known = models.BooleanField(default=False)

    class Meta:
        abstract = True

    def __unicode__(self):
        return self.display_name


class Group(StandardMetadata):
    display_name = models.CharField(max_length=200)
    description = models.TextField(blank=True, null=True)

    class Meta:
        abstract = True

    def __unicode__(self):
        return self.display_name


class Place(StandardMetadata):
    display_name = models.CharField(max_length=200)
    description = models.TextField(blank=True, null=True)
    lat = models.FloatField(blank=True, null=True)
    lon = models.FloatField(blank=True, null=True)

    class Meta:
        abstract = True

    def __unicode__(self):
        return self.display_name


class Event(StandardMetadata):
    label = models.CharField(max_length=250, blank=True, null=True)
    description = models.TextField(blank=True, null=True)
    start_earliest_date = models.DateField(null=True, blank=True)
    start_earliest_month_known = models.BooleanField(default=False)
    start_earliest_day_known = models.BooleanField(default=False)
    start_latest_date = models.DateField(null=True, blank=True)
    start_latest_month_known = models.BooleanField(default=False)
    start_latest_day_known = models.BooleanField(default=False)
    end_earliest_date = models.DateField(null=True, blank=True)
    end_earliest_month_known = models.BooleanField(default=False)
    end_earliest_day_known = models.BooleanField(default=False)
    end_latest_date = models.DateField(null=True, blank=True)
    end_latest_month_known = models.BooleanField(default=False)
    end_latest_day_known = models.BooleanField(default=False)

    def __unicode__(self):
        return self.label

    class Meta:
        abstract = True


class Period(Event):
    '''Period of time.'''

    class Meta:
        abstract = True


class URI(StandardMetadata):
    URI_TYPES = (('html', 'HTML'), ('lod_id', 'LOD id'), ('rdf_xml', 'RDF/XML'), ('rdf_turtle', 'Turtle'), ('json', 'JSON'))
    uri = models.URLField()
    uri_type = models.CharField(max_length=20, choices=URI_TYPES, default='html')

    def __unicode__(self):
        return '%s (%s)' % (self.uri, self.uri_type)

    class Meta:
        abstract = True
