# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'RecordAggregationURI'
        db.create_table('sources_recordaggregationuri', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('date_created', self.gf('django.db.models.fields.DateTimeField')(auto_now_add=True, blank=True)),
            ('date_modified', self.gf('django.db.models.fields.DateTimeField')(auto_now=True, blank=True)),
            ('uri', self.gf('django.db.models.fields.URLField')(max_length=200)),
            ('uri_type', self.gf('django.db.models.fields.CharField')(default='html', max_length=20)),
            ('aggregation', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['sources.RecordAggregation'])),
        ))
        db.send_create_signal('sources', ['RecordAggregationURI'])

        # Adding model 'RecordURI'
        db.create_table('sources_recorduri', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('date_created', self.gf('django.db.models.fields.DateTimeField')(auto_now_add=True, blank=True)),
            ('date_modified', self.gf('django.db.models.fields.DateTimeField')(auto_now=True, blank=True)),
            ('uri', self.gf('django.db.models.fields.URLField')(max_length=200)),
            ('uri_type', self.gf('django.db.models.fields.CharField')(default='html', max_length=20)),
            ('record', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['sources.Record'])),
        ))
        db.send_create_signal('sources', ['RecordURI'])

        # Adding model 'RecordAggregation'
        db.create_table('sources_recordaggregation', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('date_created', self.gf('django.db.models.fields.DateTimeField')(auto_now_add=True, blank=True)),
            ('date_modified', self.gf('django.db.models.fields.DateTimeField')(auto_now=True, blank=True)),
            ('identifier', self.gf('django.db.models.fields.CharField')(max_length=100)),
            ('numeric_identifier', self.gf('django.db.models.fields.IntegerField')(null=True, blank=True)),
            ('title', self.gf('django.db.models.fields.TextField')()),
            ('date_string', self.gf('django.db.models.fields.CharField')(max_length=50, blank=True)),
            ('start_date', self.gf('django.db.models.fields.DateField')(null=True, blank=True)),
            ('start_month_known', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('start_day_known', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('end_date', self.gf('django.db.models.fields.DateField')(null=True, blank=True)),
            ('end_month_known', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('end_day_known', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('description', self.gf('django.db.models.fields.TextField')(blank=True)),
            ('aggregation_type', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['sources.AggregationType'])),
            ('number_of_items', self.gf('django.db.models.fields.IntegerField')(null=True, blank=True)),
            ('linear_size', self.gf('django.db.models.fields.DecimalField')(null=True, max_digits=8, decimal_places=3, blank=True)),
            ('repository', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['people.Repository'], null=True, blank=True)),
        ))
        db.send_create_signal('sources', ['RecordAggregation'])

        # Adding model 'AggregationRelatedAggregation'
        db.create_table('sources_aggregationrelatedaggregation', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('aggregation', self.gf('django.db.models.fields.related.ForeignKey')(related_name='main_aggregation', to=orm['sources.RecordAggregation'])),
            ('related_aggregation', self.gf('django.db.models.fields.related.ForeignKey')(related_name='related_aggregation', to=orm['sources.RecordAggregation'])),
            ('relationship', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['sources.AggregationRelationship'])),
        ))
        db.send_create_signal('sources', ['AggregationRelatedAggregation'])

        # Adding model 'AggregationType'
        db.create_table('sources_aggregationtype', (
            ('rdftype_ptr', self.gf('django.db.models.fields.related.OneToOneField')(to=orm['linkeddata.RDFType'], unique=True, primary_key=True)),
        ))
        db.send_create_signal('sources', ['AggregationType'])

        # Adding model 'AggregationRelationship'
        db.create_table('sources_aggregationrelationship', (
            ('rdfrelationship_ptr', self.gf('django.db.models.fields.related.OneToOneField')(to=orm['linkeddata.RDFRelationship'], unique=True, primary_key=True)),
        ))
        db.send_create_signal('sources', ['AggregationRelationship'])

        # Adding model 'AggregationStats'
        db.create_table('sources_aggregationstats', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('date_created', self.gf('django.db.models.fields.DateTimeField')(auto_now_add=True, blank=True)),
            ('date_modified', self.gf('django.db.models.fields.DateTimeField')(auto_now=True, blank=True)),
            ('aggregation', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['sources.RecordAggregation'])),
            ('number_described', self.gf('django.db.models.fields.IntegerField')(max_length=8, null=True, blank=True)),
            ('number_described_note', self.gf('django.db.models.fields.TextField')(blank=True)),
            ('number_digitised', self.gf('django.db.models.fields.IntegerField')(max_length=8, null=True, blank=True)),
            ('number_digitised_pages', self.gf('django.db.models.fields.IntegerField')(null=True, blank=True)),
        ))
        db.send_create_signal('sources', ['AggregationStats'])

        # Adding model 'AggregationRelatedAgency'
        db.create_table('sources_aggregationrelatedagency', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('aggregation', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['sources.RecordAggregation'])),
            ('agency', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['people.Agency'])),
            ('relationship', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['sources.AggregationAgencyRelationship'])),
        ))
        db.send_create_signal('sources', ['AggregationRelatedAgency'])

        # Adding model 'AggregationAgencyRelationship'
        db.create_table('sources_aggregationagencyrelationship', (
            ('rdfrelationship_ptr', self.gf('django.db.models.fields.related.OneToOneField')(to=orm['linkeddata.RDFRelationship'], unique=True, primary_key=True)),
        ))
        db.send_create_signal('sources', ['AggregationAgencyRelationship'])

        # Adding model 'Record'
        db.create_table('sources_record', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('date_created', self.gf('django.db.models.fields.DateTimeField')(auto_now_add=True, blank=True)),
            ('date_modified', self.gf('django.db.models.fields.DateTimeField')(auto_now=True, blank=True)),
            ('identifier', self.gf('django.db.models.fields.CharField')(max_length=100)),
            ('numeric_identifier', self.gf('django.db.models.fields.IntegerField')(null=True, blank=True)),
            ('title', self.gf('django.db.models.fields.TextField')()),
            ('date_string', self.gf('django.db.models.fields.CharField')(max_length=50, blank=True)),
            ('start_date', self.gf('django.db.models.fields.DateField')(null=True, blank=True)),
            ('start_month_known', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('start_day_known', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('end_date', self.gf('django.db.models.fields.DateField')(null=True, blank=True)),
            ('end_month_known', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('end_day_known', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('description', self.gf('django.db.models.fields.TextField')(blank=True)),
            ('aggregation', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['sources.RecordAggregation'], null=True, blank=True)),
        ))
        db.send_create_signal('sources', ['Record'])

        # Adding model 'NSWBDMRecord'
        db.create_table('sources_nswbdmrecord', (
            ('record_ptr', self.gf('django.db.models.fields.related.OneToOneField')(to=orm['sources.Record'], unique=True, primary_key=True)),
            ('registration_year', self.gf('django.db.models.fields.IntegerField')(null=True, blank=True)),
            ('registration_number', self.gf('django.db.models.fields.IntegerField')(null=True, blank=True)),
            ('registration_place', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['places.Place'], null=True, blank=True)),
            ('volume_reference', self.gf('django.db.models.fields.CharField')(max_length=20, null=True, blank=True)),
        ))
        db.send_create_signal('sources', ['NSWBDMRecord'])

        # Adding model 'RecordRelatedResident'
        db.create_table('sources_recordrelatedresident', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('record', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['sources.Record'])),
            ('resident', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['people.Resident'])),
            ('relationship', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['sources.RecordPersonRelationship'])),
        ))
        db.send_create_signal('sources', ['RecordRelatedResident'])

        # Adding model 'RecordRelatedOfficial'
        db.create_table('sources_recordrelatedofficial', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('record', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['sources.Record'])),
            ('resident', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['people.Official'])),
            ('relationship', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['sources.RecordPersonRelationship'])),
        ))
        db.send_create_signal('sources', ['RecordRelatedOfficial'])

        # Adding model 'RecordPersonRelationship'
        db.create_table('sources_recordpersonrelationship', (
            ('rdfrelationship_ptr', self.gf('django.db.models.fields.related.OneToOneField')(to=orm['linkeddata.RDFRelationship'], unique=True, primary_key=True)),
        ))
        db.send_create_signal('sources', ['RecordPersonRelationship'])

        # Adding model 'Photograph'
        db.create_table('sources_photograph', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
        ))
        db.send_create_signal('sources', ['Photograph'])

        # Adding model 'Publication'
        db.create_table('sources_publication', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
        ))
        db.send_create_signal('sources', ['Publication'])


    def backwards(self, orm):
        # Deleting model 'RecordAggregationURI'
        db.delete_table('sources_recordaggregationuri')

        # Deleting model 'RecordURI'
        db.delete_table('sources_recorduri')

        # Deleting model 'RecordAggregation'
        db.delete_table('sources_recordaggregation')

        # Deleting model 'AggregationRelatedAggregation'
        db.delete_table('sources_aggregationrelatedaggregation')

        # Deleting model 'AggregationType'
        db.delete_table('sources_aggregationtype')

        # Deleting model 'AggregationRelationship'
        db.delete_table('sources_aggregationrelationship')

        # Deleting model 'AggregationStats'
        db.delete_table('sources_aggregationstats')

        # Deleting model 'AggregationRelatedAgency'
        db.delete_table('sources_aggregationrelatedagency')

        # Deleting model 'AggregationAgencyRelationship'
        db.delete_table('sources_aggregationagencyrelationship')

        # Deleting model 'Record'
        db.delete_table('sources_record')

        # Deleting model 'NSWBDMRecord'
        db.delete_table('sources_nswbdmrecord')

        # Deleting model 'RecordRelatedResident'
        db.delete_table('sources_recordrelatedresident')

        # Deleting model 'RecordRelatedOfficial'
        db.delete_table('sources_recordrelatedofficial')

        # Deleting model 'RecordPersonRelationship'
        db.delete_table('sources_recordpersonrelationship')

        # Deleting model 'Photograph'
        db.delete_table('sources_photograph')

        # Deleting model 'Publication'
        db.delete_table('sources_publication')


    models = {
        'linkeddata.rdfclass': {
            'Meta': {'object_name': 'RDFClass'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'rdf_class': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'schema': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['linkeddata.RDFSchema']"})
        },
        'linkeddata.rdfproperty': {
            'Meta': {'object_name': 'RDFProperty'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'inverse': ('django.db.models.fields.CharField', [], {'max_length': '50', 'null': 'True', 'blank': 'True'}),
            'rdf_property': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'schema': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['linkeddata.RDFSchema']"})
        },
        'linkeddata.rdfrelationship': {
            'Meta': {'object_name': 'RDFRelationship'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'label': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'rdf_property': ('django.db.models.fields.related.ManyToManyField', [], {'symmetrical': 'False', 'to': "orm['linkeddata.RDFProperty']", 'null': 'True', 'blank': 'True'})
        },
        'linkeddata.rdfschema': {
            'Meta': {'object_name': 'RDFSchema'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'prefix': ('django.db.models.fields.CharField', [], {'max_length': '20'}),
            'uri': ('django.db.models.fields.CharField', [], {'max_length': '200'})
        },
        'linkeddata.rdftype': {
            'Meta': {'object_name': 'RDFType'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'label': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'rdf_class': ('django.db.models.fields.related.ManyToManyField', [], {'symmetrical': 'False', 'to': "orm['linkeddata.RDFClass']", 'null': 'True', 'blank': 'True'})
        },
        'people.agency': {
            'Meta': {'object_name': 'Agency'},
            'date_created': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'date_modified': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'}),
            'description': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'display_name': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'})
        },
        'people.official': {
            'Meta': {'object_name': 'Official'},
            'biography': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'birth_earliest_date': ('django.db.models.fields.DateField', [], {'null': 'True', 'blank': 'True'}),
            'birth_earliest_day_known': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'birth_earliest_month_known': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'birth_latest_date': ('django.db.models.fields.DateField', [], {'null': 'True', 'blank': 'True'}),
            'birth_latest_day_known': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'birth_latest_month_known': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'birth_place': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "'people_official_birth_place'", 'null': 'True', 'to': "orm['places.Place']"}),
            'date_created': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'date_modified': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'}),
            'death_earliest_date': ('django.db.models.fields.DateField', [], {'null': 'True', 'blank': 'True'}),
            'death_earliest_day_known': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'death_earliest_month_known': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'death_latest_date': ('django.db.models.fields.DateField', [], {'null': 'True', 'blank': 'True'}),
            'death_latest_day_known': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'death_latest_month_known': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'death_place': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "'people_official_death_place'", 'null': 'True', 'to': "orm['places.Place']"}),
            'display_name': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'})
        },
        'people.repository': {
            'Meta': {'object_name': 'Repository'},
            'date_created': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'date_modified': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'}),
            'description': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'display_name': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'})
        },
        'people.resident': {
            'Meta': {'object_name': 'Resident'},
            'biography': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'birth_earliest_date': ('django.db.models.fields.DateField', [], {'null': 'True', 'blank': 'True'}),
            'birth_earliest_day_known': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'birth_earliest_month_known': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'birth_latest_date': ('django.db.models.fields.DateField', [], {'null': 'True', 'blank': 'True'}),
            'birth_latest_day_known': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'birth_latest_month_known': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'birth_place': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "'people_resident_birth_place'", 'null': 'True', 'to': "orm['places.Place']"}),
            'date_created': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'date_modified': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'}),
            'death_earliest_date': ('django.db.models.fields.DateField', [], {'null': 'True', 'blank': 'True'}),
            'death_earliest_day_known': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'death_earliest_month_known': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'death_latest_date': ('django.db.models.fields.DateField', [], {'null': 'True', 'blank': 'True'}),
            'death_latest_day_known': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'death_latest_month_known': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'death_place': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "'people_resident_death_place'", 'null': 'True', 'to': "orm['places.Place']"}),
            'display_name': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'papertrails': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'related_people': ('django.db.models.fields.related.ManyToManyField', [], {'symmetrical': 'False', 'to': "orm['people.Resident']", 'null': 'True', 'through': "orm['people.ResidentRelatedResident']", 'blank': 'True'})
        },
        'people.residentrelatedresident': {
            'Meta': {'object_name': 'ResidentRelatedResident'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'related_resident': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'related_resident'", 'to': "orm['people.Resident']"}),
            'relationship': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['people.ResidentRelationship']"}),
            'resident': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'main_resident'", 'to': "orm['people.Resident']"})
        },
        'people.residentrelationship': {
            'Meta': {'object_name': 'ResidentRelationship', '_ormbases': ['linkeddata.RDFRelationship']},
            'rdfrelationship_ptr': ('django.db.models.fields.related.OneToOneField', [], {'to': "orm['linkeddata.RDFRelationship']", 'unique': 'True', 'primary_key': 'True'})
        },
        'places.place': {
            'Meta': {'object_name': 'Place'},
            'date_created': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'date_modified': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'}),
            'description': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'display_name': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'lat': ('django.db.models.fields.FloatField', [], {'null': 'True', 'blank': 'True'}),
            'lon': ('django.db.models.fields.FloatField', [], {'null': 'True', 'blank': 'True'}),
            'related_places': ('django.db.models.fields.related.ManyToManyField', [], {'symmetrical': 'False', 'to': "orm['places.Place']", 'null': 'True', 'through': "orm['places.PlaceRelatedPlace']", 'blank': 'True'})
        },
        'places.placerelatedplace': {
            'Meta': {'object_name': 'PlaceRelatedPlace'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'place': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'main_place'", 'to': "orm['places.Place']"}),
            'related_place': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'related_place'", 'to': "orm['places.Place']"}),
            'relationship': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['places.PlaceRelationship']"})
        },
        'places.placerelationship': {
            'Meta': {'object_name': 'PlaceRelationship', '_ormbases': ['linkeddata.RDFRelationship']},
            'rdfrelationship_ptr': ('django.db.models.fields.related.OneToOneField', [], {'to': "orm['linkeddata.RDFRelationship']", 'unique': 'True', 'primary_key': 'True'})
        },
        'sources.aggregationagencyrelationship': {
            'Meta': {'object_name': 'AggregationAgencyRelationship', '_ormbases': ['linkeddata.RDFRelationship']},
            'rdfrelationship_ptr': ('django.db.models.fields.related.OneToOneField', [], {'to': "orm['linkeddata.RDFRelationship']", 'unique': 'True', 'primary_key': 'True'})
        },
        'sources.aggregationrelatedagency': {
            'Meta': {'object_name': 'AggregationRelatedAgency'},
            'agency': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['people.Agency']"}),
            'aggregation': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['sources.RecordAggregation']"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'relationship': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['sources.AggregationAgencyRelationship']"})
        },
        'sources.aggregationrelatedaggregation': {
            'Meta': {'object_name': 'AggregationRelatedAggregation'},
            'aggregation': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'main_aggregation'", 'to': "orm['sources.RecordAggregation']"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'related_aggregation': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'related_aggregation'", 'to': "orm['sources.RecordAggregation']"}),
            'relationship': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['sources.AggregationRelationship']"})
        },
        'sources.aggregationrelationship': {
            'Meta': {'object_name': 'AggregationRelationship', '_ormbases': ['linkeddata.RDFRelationship']},
            'rdfrelationship_ptr': ('django.db.models.fields.related.OneToOneField', [], {'to': "orm['linkeddata.RDFRelationship']", 'unique': 'True', 'primary_key': 'True'})
        },
        'sources.aggregationstats': {
            'Meta': {'object_name': 'AggregationStats'},
            'aggregation': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['sources.RecordAggregation']"}),
            'date_created': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'date_modified': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'number_described': ('django.db.models.fields.IntegerField', [], {'max_length': '8', 'null': 'True', 'blank': 'True'}),
            'number_described_note': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'number_digitised': ('django.db.models.fields.IntegerField', [], {'max_length': '8', 'null': 'True', 'blank': 'True'}),
            'number_digitised_pages': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'})
        },
        'sources.aggregationtype': {
            'Meta': {'object_name': 'AggregationType', '_ormbases': ['linkeddata.RDFType']},
            'rdftype_ptr': ('django.db.models.fields.related.OneToOneField', [], {'to': "orm['linkeddata.RDFType']", 'unique': 'True', 'primary_key': 'True'})
        },
        'sources.nswbdmrecord': {
            'Meta': {'object_name': 'NSWBDMRecord', '_ormbases': ['sources.Record']},
            'record_ptr': ('django.db.models.fields.related.OneToOneField', [], {'to': "orm['sources.Record']", 'unique': 'True', 'primary_key': 'True'}),
            'registration_number': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'registration_place': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['places.Place']", 'null': 'True', 'blank': 'True'}),
            'registration_year': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'volume_reference': ('django.db.models.fields.CharField', [], {'max_length': '20', 'null': 'True', 'blank': 'True'})
        },
        'sources.photograph': {
            'Meta': {'object_name': 'Photograph'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'})
        },
        'sources.publication': {
            'Meta': {'object_name': 'Publication'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'})
        },
        'sources.record': {
            'Meta': {'object_name': 'Record'},
            'aggregation': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['sources.RecordAggregation']", 'null': 'True', 'blank': 'True'}),
            'date_created': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'date_modified': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'}),
            'date_string': ('django.db.models.fields.CharField', [], {'max_length': '50', 'blank': 'True'}),
            'description': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'end_date': ('django.db.models.fields.DateField', [], {'null': 'True', 'blank': 'True'}),
            'end_day_known': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'end_month_known': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'identifier': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'numeric_identifier': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'related_officials': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['people.Official']", 'through': "orm['sources.RecordRelatedOfficial']", 'symmetrical': 'False'}),
            'related_residents': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['people.Resident']", 'through': "orm['sources.RecordRelatedResident']", 'symmetrical': 'False'}),
            'start_date': ('django.db.models.fields.DateField', [], {'null': 'True', 'blank': 'True'}),
            'start_day_known': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'start_month_known': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'title': ('django.db.models.fields.TextField', [], {})
        },
        'sources.recordaggregation': {
            'Meta': {'object_name': 'RecordAggregation'},
            'agencies': ('django.db.models.fields.related.ManyToManyField', [], {'symmetrical': 'False', 'to': "orm['people.Agency']", 'null': 'True', 'through': "orm['sources.AggregationRelatedAgency']", 'blank': 'True'}),
            'aggregation_type': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['sources.AggregationType']"}),
            'date_created': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'date_modified': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'}),
            'date_string': ('django.db.models.fields.CharField', [], {'max_length': '50', 'blank': 'True'}),
            'description': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'end_date': ('django.db.models.fields.DateField', [], {'null': 'True', 'blank': 'True'}),
            'end_day_known': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'end_month_known': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'identifier': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'linear_size': ('django.db.models.fields.DecimalField', [], {'null': 'True', 'max_digits': '8', 'decimal_places': '3', 'blank': 'True'}),
            'number_of_items': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'numeric_identifier': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'related_aggregations': ('django.db.models.fields.related.ManyToManyField', [], {'symmetrical': 'False', 'to': "orm['sources.RecordAggregation']", 'null': 'True', 'through': "orm['sources.AggregationRelatedAggregation']", 'blank': 'True'}),
            'repository': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['people.Repository']", 'null': 'True', 'blank': 'True'}),
            'start_date': ('django.db.models.fields.DateField', [], {'null': 'True', 'blank': 'True'}),
            'start_day_known': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'start_month_known': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'title': ('django.db.models.fields.TextField', [], {})
        },
        'sources.recordaggregationuri': {
            'Meta': {'object_name': 'RecordAggregationURI'},
            'aggregation': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['sources.RecordAggregation']"}),
            'date_created': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'date_modified': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'uri': ('django.db.models.fields.URLField', [], {'max_length': '200'}),
            'uri_type': ('django.db.models.fields.CharField', [], {'default': "'html'", 'max_length': '20'})
        },
        'sources.recordpersonrelationship': {
            'Meta': {'object_name': 'RecordPersonRelationship', '_ormbases': ['linkeddata.RDFRelationship']},
            'rdfrelationship_ptr': ('django.db.models.fields.related.OneToOneField', [], {'to': "orm['linkeddata.RDFRelationship']", 'unique': 'True', 'primary_key': 'True'})
        },
        'sources.recordrelatedofficial': {
            'Meta': {'object_name': 'RecordRelatedOfficial'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'record': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['sources.Record']"}),
            'relationship': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['sources.RecordPersonRelationship']"}),
            'resident': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['people.Official']"})
        },
        'sources.recordrelatedresident': {
            'Meta': {'object_name': 'RecordRelatedResident'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'record': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['sources.Record']"}),
            'relationship': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['sources.RecordPersonRelationship']"}),
            'resident': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['people.Resident']"})
        },
        'sources.recorduri': {
            'Meta': {'object_name': 'RecordURI'},
            'date_created': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'date_modified': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'record': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['sources.Record']"}),
            'uri': ('django.db.models.fields.URLField', [], {'max_length': '200'}),
            'uri_type': ('django.db.models.fields.CharField', [], {'default': "'html'", 'max_length': '20'})
        }
    }

    complete_apps = ['sources']