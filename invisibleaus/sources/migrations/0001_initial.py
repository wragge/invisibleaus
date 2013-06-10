# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
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
            ('is_part_of', self.gf('django.db.models.fields.related.ForeignKey')(blank=True, related_name='part_of', null=True, to=orm['sources.Record'])),
            ('record_type', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['sources.RecordType'])),
            ('number_of_items', self.gf('django.db.models.fields.IntegerField')(null=True, blank=True)),
            ('repository', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['people.Repository'], null=True, blank=True)),
            ('access_status', self.gf('django.db.models.fields.CharField')(max_length=30, null=True, blank=True)),
            ('long_citation', self.gf('django.db.models.fields.TextField')(null=True, blank=True)),
            ('short_citation', self.gf('django.db.models.fields.CharField')(max_length=100, null=True, blank=True)),
            ('start_page', self.gf('django.db.models.fields.IntegerField')(null=True, blank=True)),
            ('end_page', self.gf('django.db.models.fields.IntegerField')(null=True, blank=True)),
        ))
        db.send_create_signal('sources', ['Record'])

        # Adding model 'RecordRelatedRecord'
        db.create_table('sources_recordrelatedrecord', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('record', self.gf('django.db.models.fields.related.ForeignKey')(related_name='main_record', to=orm['sources.Record'])),
            ('related_record', self.gf('django.db.models.fields.related.ForeignKey')(related_name='related_record', to=orm['sources.Record'])),
            ('relationship', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['sources.RecordRelationship'])),
        ))
        db.send_create_signal('sources', ['RecordRelatedRecord'])

        # Adding model 'RecordType'
        db.create_table('sources_recordtype', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('label', self.gf('django.db.models.fields.CharField')(max_length=50)),
        ))
        db.send_create_signal('sources', ['RecordType'])

        # Adding M2M table for field rdf_class on 'RecordType'
        db.create_table('sources_recordtype_rdf_class', (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('recordtype', models.ForeignKey(orm['sources.recordtype'], null=False)),
            ('rdfclass', models.ForeignKey(orm['linkeddata.rdfclass'], null=False))
        ))
        db.create_unique('sources_recordtype_rdf_class', ['recordtype_id', 'rdfclass_id'])

        # Adding model 'RecordRelationship'
        db.create_table('sources_recordrelationship', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('label', self.gf('django.db.models.fields.CharField')(max_length=50)),
        ))
        db.send_create_signal('sources', ['RecordRelationship'])

        # Adding M2M table for field rdf_property on 'RecordRelationship'
        db.create_table('sources_recordrelationship_rdf_property', (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('recordrelationship', models.ForeignKey(orm['sources.recordrelationship'], null=False)),
            ('rdfproperty', models.ForeignKey(orm['linkeddata.rdfproperty'], null=False))
        ))
        db.create_unique('sources_recordrelationship_rdf_property', ['recordrelationship_id', 'rdfproperty_id'])

        # Adding model 'RecordStats'
        db.create_table('sources_recordstats', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('date_created', self.gf('django.db.models.fields.DateTimeField')(auto_now_add=True, blank=True)),
            ('date_modified', self.gf('django.db.models.fields.DateTimeField')(auto_now=True, blank=True)),
            ('record', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['sources.Record'])),
            ('number_described', self.gf('django.db.models.fields.IntegerField')(null=True, blank=True)),
            ('number_described_note', self.gf('django.db.models.fields.TextField')(blank=True)),
            ('number_digitised', self.gf('django.db.models.fields.IntegerField')(null=True, blank=True)),
            ('linear_size', self.gf('django.db.models.fields.DecimalField')(null=True, max_digits=8, decimal_places=3, blank=True)),
        ))
        db.send_create_signal('sources', ['RecordStats'])

        # Adding model 'NSWBDMRecord'
        db.create_table('sources_nswbdmrecord', (
            ('record_ptr', self.gf('django.db.models.fields.related.OneToOneField')(to=orm['sources.Record'], unique=True, primary_key=True)),
            ('registration_year', self.gf('django.db.models.fields.IntegerField')(null=True, blank=True)),
            ('registration_number', self.gf('django.db.models.fields.IntegerField')(null=True, blank=True)),
            ('registration_place', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['places.Place'], null=True, blank=True)),
            ('volume_reference', self.gf('django.db.models.fields.CharField')(max_length=20, null=True, blank=True)),
        ))
        db.send_create_signal('sources', ['NSWBDMRecord'])

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
        # Deleting model 'RecordURI'
        db.delete_table('sources_recorduri')

        # Deleting model 'Record'
        db.delete_table('sources_record')

        # Deleting model 'RecordRelatedRecord'
        db.delete_table('sources_recordrelatedrecord')

        # Deleting model 'RecordType'
        db.delete_table('sources_recordtype')

        # Removing M2M table for field rdf_class on 'RecordType'
        db.delete_table('sources_recordtype_rdf_class')

        # Deleting model 'RecordRelationship'
        db.delete_table('sources_recordrelationship')

        # Removing M2M table for field rdf_property on 'RecordRelationship'
        db.delete_table('sources_recordrelationship_rdf_property')

        # Deleting model 'RecordStats'
        db.delete_table('sources_recordstats')

        # Deleting model 'NSWBDMRecord'
        db.delete_table('sources_nswbdmrecord')

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
        'linkeddata.rdfschema': {
            'Meta': {'object_name': 'RDFSchema'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'prefix': ('django.db.models.fields.CharField', [], {'max_length': '20'}),
            'uri': ('django.db.models.fields.CharField', [], {'max_length': '200'})
        },
        'people.repository': {
            'Meta': {'object_name': 'Repository'},
            'date_created': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'date_modified': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'}),
            'description': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'display_name': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'})
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
            'Meta': {'object_name': 'PlaceRelationship'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'label': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'rdf_property': ('django.db.models.fields.related.ManyToManyField', [], {'symmetrical': 'False', 'to': "orm['linkeddata.RDFProperty']", 'null': 'True', 'blank': 'True'})
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
            'access_status': ('django.db.models.fields.CharField', [], {'max_length': '30', 'null': 'True', 'blank': 'True'}),
            'date_created': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'date_modified': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'}),
            'date_string': ('django.db.models.fields.CharField', [], {'max_length': '50', 'blank': 'True'}),
            'description': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'end_date': ('django.db.models.fields.DateField', [], {'null': 'True', 'blank': 'True'}),
            'end_day_known': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'end_month_known': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'end_page': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'identifier': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'is_part_of': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "'part_of'", 'null': 'True', 'to': "orm['sources.Record']"}),
            'long_citation': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'number_of_items': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'numeric_identifier': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'record_type': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['sources.RecordType']"}),
            'related_records': ('django.db.models.fields.related.ManyToManyField', [], {'symmetrical': 'False', 'to': "orm['sources.Record']", 'null': 'True', 'through': "orm['sources.RecordRelatedRecord']", 'blank': 'True'}),
            'repository': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['people.Repository']", 'null': 'True', 'blank': 'True'}),
            'short_citation': ('django.db.models.fields.CharField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'start_date': ('django.db.models.fields.DateField', [], {'null': 'True', 'blank': 'True'}),
            'start_day_known': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'start_month_known': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'start_page': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'title': ('django.db.models.fields.TextField', [], {})
        },
        'sources.recordrelatedrecord': {
            'Meta': {'object_name': 'RecordRelatedRecord'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'record': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'main_record'", 'to': "orm['sources.Record']"}),
            'related_record': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'related_record'", 'to': "orm['sources.Record']"}),
            'relationship': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['sources.RecordRelationship']"})
        },
        'sources.recordrelationship': {
            'Meta': {'object_name': 'RecordRelationship'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'label': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'rdf_property': ('django.db.models.fields.related.ManyToManyField', [], {'symmetrical': 'False', 'to': "orm['linkeddata.RDFProperty']", 'null': 'True', 'blank': 'True'})
        },
        'sources.recordstats': {
            'Meta': {'object_name': 'RecordStats'},
            'date_created': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'date_modified': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'linear_size': ('django.db.models.fields.DecimalField', [], {'null': 'True', 'max_digits': '8', 'decimal_places': '3', 'blank': 'True'}),
            'number_described': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'number_described_note': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'number_digitised': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'record': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['sources.Record']"})
        },
        'sources.recordtype': {
            'Meta': {'object_name': 'RecordType'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'label': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'rdf_class': ('django.db.models.fields.related.ManyToManyField', [], {'symmetrical': 'False', 'to': "orm['linkeddata.RDFClass']", 'null': 'True', 'blank': 'True'})
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