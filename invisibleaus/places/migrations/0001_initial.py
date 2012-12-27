# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Place'
        db.create_table('places_place', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('date_created', self.gf('django.db.models.fields.DateTimeField')(auto_now_add=True, blank=True)),
            ('date_modified', self.gf('django.db.models.fields.DateTimeField')(auto_now=True, blank=True)),
            ('display_name', self.gf('django.db.models.fields.CharField')(max_length=200)),
            ('description', self.gf('django.db.models.fields.TextField')(null=True, blank=True)),
            ('lat', self.gf('django.db.models.fields.FloatField')(null=True, blank=True)),
            ('lon', self.gf('django.db.models.fields.FloatField')(null=True, blank=True)),
        ))
        db.send_create_signal('places', ['Place'])

        # Adding model 'PlaceRelatedPlace'
        db.create_table('places_placerelatedplace', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('place', self.gf('django.db.models.fields.related.ForeignKey')(related_name='main_place', to=orm['places.Place'])),
            ('related_place', self.gf('django.db.models.fields.related.ForeignKey')(related_name='related_place', to=orm['places.Place'])),
            ('relationship', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['places.PlaceRelationship'])),
        ))
        db.send_create_signal('places', ['PlaceRelatedPlace'])

        # Adding model 'PlaceRelationship'
        db.create_table('places_placerelationship', (
            ('rdfrelationship_ptr', self.gf('django.db.models.fields.related.OneToOneField')(to=orm['linkeddata.RDFRelationship'], unique=True, primary_key=True)),
        ))
        db.send_create_signal('places', ['PlaceRelationship'])


    def backwards(self, orm):
        # Deleting model 'Place'
        db.delete_table('places_place')

        # Deleting model 'PlaceRelatedPlace'
        db.delete_table('places_placerelatedplace')

        # Deleting model 'PlaceRelationship'
        db.delete_table('places_placerelationship')


    models = {
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
        }
    }

    complete_apps = ['places']