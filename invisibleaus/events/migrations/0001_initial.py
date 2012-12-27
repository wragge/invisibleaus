# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'SeaVoyage'
        db.create_table('events_seavoyage', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('date_created', self.gf('django.db.models.fields.DateTimeField')(auto_now_add=True, blank=True)),
            ('date_modified', self.gf('django.db.models.fields.DateTimeField')(auto_now=True, blank=True)),
            ('label', self.gf('django.db.models.fields.CharField')(max_length=250, null=True, blank=True)),
            ('description', self.gf('django.db.models.fields.TextField')(null=True, blank=True)),
            ('start_earliest_date', self.gf('django.db.models.fields.DateField')(null=True, blank=True)),
            ('start_earliest_month_known', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('start_earliest_day_known', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('start_latest_date', self.gf('django.db.models.fields.DateField')(null=True, blank=True)),
            ('start_latest_month_known', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('start_latest_day_known', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('end_earliest_date', self.gf('django.db.models.fields.DateField')(null=True, blank=True)),
            ('end_earliest_month_known', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('end_earliest_day_known', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('end_latest_date', self.gf('django.db.models.fields.DateField')(null=True, blank=True)),
            ('end_latest_month_known', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('end_latest_day_known', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('embarkation_place', self.gf('django.db.models.fields.related.ForeignKey')(related_name='embarkation_place', to=orm['places.Place'])),
            ('destination_place', self.gf('django.db.models.fields.related.ForeignKey')(related_name='destination_place', to=orm['places.Place'])),
            ('ship', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['things.Ship'])),
        ))
        db.send_create_signal('events', ['SeaVoyage'])

        # Adding model 'SeaVoyageLeg'
        db.create_table('events_seavoyageleg', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('date_created', self.gf('django.db.models.fields.DateTimeField')(auto_now_add=True, blank=True)),
            ('date_modified', self.gf('django.db.models.fields.DateTimeField')(auto_now=True, blank=True)),
            ('label', self.gf('django.db.models.fields.CharField')(max_length=250, null=True, blank=True)),
            ('description', self.gf('django.db.models.fields.TextField')(null=True, blank=True)),
            ('start_earliest_date', self.gf('django.db.models.fields.DateField')(null=True, blank=True)),
            ('start_earliest_month_known', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('start_earliest_day_known', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('start_latest_date', self.gf('django.db.models.fields.DateField')(null=True, blank=True)),
            ('start_latest_month_known', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('start_latest_day_known', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('end_earliest_date', self.gf('django.db.models.fields.DateField')(null=True, blank=True)),
            ('end_earliest_month_known', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('end_earliest_day_known', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('end_latest_date', self.gf('django.db.models.fields.DateField')(null=True, blank=True)),
            ('end_latest_month_known', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('end_latest_day_known', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('start_place', self.gf('django.db.models.fields.related.ForeignKey')(blank=True, related_name='events_seavoyageleg_start_place', null=True, to=orm['places.Place'])),
            ('end_place', self.gf('django.db.models.fields.related.ForeignKey')(blank=True, related_name='events_seavoyageleg_end_place', null=True, to=orm['places.Place'])),
            ('sea_voyage', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['events.SeaVoyage'])),
        ))
        db.send_create_signal('events', ['SeaVoyageLeg'])


    def backwards(self, orm):
        # Deleting model 'SeaVoyage'
        db.delete_table('events_seavoyage')

        # Deleting model 'SeaVoyageLeg'
        db.delete_table('events_seavoyageleg')


    models = {
        'events.seavoyage': {
            'Meta': {'object_name': 'SeaVoyage'},
            'date_created': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'date_modified': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'}),
            'description': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'destination_place': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'destination_place'", 'to': "orm['places.Place']"}),
            'embarkation_place': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'embarkation_place'", 'to': "orm['places.Place']"}),
            'end_earliest_date': ('django.db.models.fields.DateField', [], {'null': 'True', 'blank': 'True'}),
            'end_earliest_day_known': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'end_earliest_month_known': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'end_latest_date': ('django.db.models.fields.DateField', [], {'null': 'True', 'blank': 'True'}),
            'end_latest_day_known': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'end_latest_month_known': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'label': ('django.db.models.fields.CharField', [], {'max_length': '250', 'null': 'True', 'blank': 'True'}),
            'ship': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['things.Ship']"}),
            'start_earliest_date': ('django.db.models.fields.DateField', [], {'null': 'True', 'blank': 'True'}),
            'start_earliest_day_known': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'start_earliest_month_known': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'start_latest_date': ('django.db.models.fields.DateField', [], {'null': 'True', 'blank': 'True'}),
            'start_latest_day_known': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'start_latest_month_known': ('django.db.models.fields.BooleanField', [], {'default': 'False'})
        },
        'events.seavoyageleg': {
            'Meta': {'object_name': 'SeaVoyageLeg'},
            'date_created': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'date_modified': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'}),
            'description': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'end_earliest_date': ('django.db.models.fields.DateField', [], {'null': 'True', 'blank': 'True'}),
            'end_earliest_day_known': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'end_earliest_month_known': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'end_latest_date': ('django.db.models.fields.DateField', [], {'null': 'True', 'blank': 'True'}),
            'end_latest_day_known': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'end_latest_month_known': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'end_place': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "'events_seavoyageleg_end_place'", 'null': 'True', 'to': "orm['places.Place']"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'label': ('django.db.models.fields.CharField', [], {'max_length': '250', 'null': 'True', 'blank': 'True'}),
            'sea_voyage': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['events.SeaVoyage']"}),
            'start_earliest_date': ('django.db.models.fields.DateField', [], {'null': 'True', 'blank': 'True'}),
            'start_earliest_day_known': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'start_earliest_month_known': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'start_latest_date': ('django.db.models.fields.DateField', [], {'null': 'True', 'blank': 'True'}),
            'start_latest_day_known': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'start_latest_month_known': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'start_place': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "'events_seavoyageleg_start_place'", 'null': 'True', 'to': "orm['places.Place']"})
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
        'things.ship': {
            'Meta': {'object_name': 'Ship'},
            'date_created': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'date_modified': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'}),
            'description': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'label': ('django.db.models.fields.CharField', [], {'max_length': '250', 'null': 'True', 'blank': 'True'})
        }
    }

    complete_apps = ['events']