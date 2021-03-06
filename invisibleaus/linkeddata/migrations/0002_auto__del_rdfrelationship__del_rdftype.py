# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Deleting model 'RDFRelationship'
        db.delete_table('linkeddata_rdfrelationship')

        # Removing M2M table for field rdf_property on 'RDFRelationship'
        db.delete_table('linkeddata_rdfrelationship_rdf_property')

        # Deleting model 'RDFType'
        db.delete_table('linkeddata_rdftype')

        # Removing M2M table for field rdf_class on 'RDFType'
        db.delete_table('linkeddata_rdftype_rdf_class')


    def backwards(self, orm):
        # Adding model 'RDFRelationship'
        db.create_table('linkeddata_rdfrelationship', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('label', self.gf('django.db.models.fields.CharField')(max_length=50)),
        ))
        db.send_create_signal('linkeddata', ['RDFRelationship'])

        # Adding M2M table for field rdf_property on 'RDFRelationship'
        db.create_table('linkeddata_rdfrelationship_rdf_property', (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('rdfrelationship', models.ForeignKey(orm['linkeddata.rdfrelationship'], null=False)),
            ('rdfproperty', models.ForeignKey(orm['linkeddata.rdfproperty'], null=False))
        ))
        db.create_unique('linkeddata_rdfrelationship_rdf_property', ['rdfrelationship_id', 'rdfproperty_id'])

        # Adding model 'RDFType'
        db.create_table('linkeddata_rdftype', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('label', self.gf('django.db.models.fields.CharField')(max_length=50)),
        ))
        db.send_create_signal('linkeddata', ['RDFType'])

        # Adding M2M table for field rdf_class on 'RDFType'
        db.create_table('linkeddata_rdftype_rdf_class', (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('rdftype', models.ForeignKey(orm['linkeddata.rdftype'], null=False)),
            ('rdfclass', models.ForeignKey(orm['linkeddata.rdfclass'], null=False))
        ))
        db.create_unique('linkeddata_rdftype_rdf_class', ['rdftype_id', 'rdfclass_id'])


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
        }
    }

    complete_apps = ['linkeddata']