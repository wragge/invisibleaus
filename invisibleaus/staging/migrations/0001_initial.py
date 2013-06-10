# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'NSWBDMRegister'
        db.create_table('staging_nswbdmregister', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('surname', self.gf('django.db.models.fields.CharField')(max_length=100, null=True, blank=True)),
            ('given_names', self.gf('django.db.models.fields.CharField')(max_length=100, null=True, blank=True)),
            ('event_type', self.gf('django.db.models.fields.CharField')(max_length=1, null=True, blank=True)),
            ('index_year', self.gf('django.db.models.fields.IntegerField')(null=True, blank=True)),
            ('father_spouse_surname', self.gf('django.db.models.fields.CharField')(max_length=100, null=True, blank=True)),
            ('mother_spouses_names', self.gf('django.db.models.fields.CharField')(max_length=100, null=True, blank=True)),
            ('registration_place', self.gf('django.db.models.fields.CharField')(max_length=100, null=True, blank=True)),
            ('volume_reference', self.gf('django.db.models.fields.CharField')(max_length=20, null=True, blank=True)),
            ('registration_year', self.gf('django.db.models.fields.IntegerField')(null=True, blank=True)),
            ('registration_number', self.gf('django.db.models.fields.CharField')(max_length=20, null=True, blank=True)),
        ))
        db.send_create_signal('staging', ['NSWBDMRegister'])


    def backwards(self, orm):
        # Deleting model 'NSWBDMRegister'
        db.delete_table('staging_nswbdmregister')


    models = {
        'staging.nswbdmregister': {
            'Meta': {'object_name': 'NSWBDMRegister'},
            'event_type': ('django.db.models.fields.CharField', [], {'max_length': '1', 'null': 'True', 'blank': 'True'}),
            'father_spouse_surname': ('django.db.models.fields.CharField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'given_names': ('django.db.models.fields.CharField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'index_year': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'mother_spouses_names': ('django.db.models.fields.CharField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'registration_number': ('django.db.models.fields.CharField', [], {'max_length': '20', 'null': 'True', 'blank': 'True'}),
            'registration_place': ('django.db.models.fields.CharField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'registration_year': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'surname': ('django.db.models.fields.CharField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'volume_reference': ('django.db.models.fields.CharField', [], {'max_length': '20', 'null': 'True', 'blank': 'True'})
        }
    }

    complete_apps = ['staging']