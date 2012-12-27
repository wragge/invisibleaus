# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Resident'
        db.create_table('people_resident', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('date_created', self.gf('django.db.models.fields.DateTimeField')(auto_now_add=True, blank=True)),
            ('date_modified', self.gf('django.db.models.fields.DateTimeField')(auto_now=True, blank=True)),
            ('display_name', self.gf('django.db.models.fields.CharField')(max_length=200)),
            ('biography', self.gf('django.db.models.fields.TextField')(null=True, blank=True)),
            ('birth_earliest_date', self.gf('django.db.models.fields.DateField')(null=True, blank=True)),
            ('birth_earliest_month_known', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('birth_earliest_day_known', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('birth_latest_date', self.gf('django.db.models.fields.DateField')(null=True, blank=True)),
            ('birth_latest_month_known', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('birth_latest_day_known', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('death_earliest_date', self.gf('django.db.models.fields.DateField')(null=True, blank=True)),
            ('death_earliest_month_known', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('death_earliest_day_known', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('death_latest_date', self.gf('django.db.models.fields.DateField')(null=True, blank=True)),
            ('death_latest_month_known', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('death_latest_day_known', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('birth_place', self.gf('django.db.models.fields.related.ForeignKey')(blank=True, related_name='people_resident_birth_place', null=True, to=orm['places.Place'])),
            ('death_place', self.gf('django.db.models.fields.related.ForeignKey')(blank=True, related_name='people_resident_death_place', null=True, to=orm['places.Place'])),
            ('papertrails', self.gf('django.db.models.fields.BooleanField')(default=False)),
        ))
        db.send_create_signal('people', ['Resident'])

        # Adding model 'Official'
        db.create_table('people_official', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('date_created', self.gf('django.db.models.fields.DateTimeField')(auto_now_add=True, blank=True)),
            ('date_modified', self.gf('django.db.models.fields.DateTimeField')(auto_now=True, blank=True)),
            ('display_name', self.gf('django.db.models.fields.CharField')(max_length=200)),
            ('biography', self.gf('django.db.models.fields.TextField')(null=True, blank=True)),
            ('birth_earliest_date', self.gf('django.db.models.fields.DateField')(null=True, blank=True)),
            ('birth_earliest_month_known', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('birth_earliest_day_known', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('birth_latest_date', self.gf('django.db.models.fields.DateField')(null=True, blank=True)),
            ('birth_latest_month_known', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('birth_latest_day_known', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('death_earliest_date', self.gf('django.db.models.fields.DateField')(null=True, blank=True)),
            ('death_earliest_month_known', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('death_earliest_day_known', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('death_latest_date', self.gf('django.db.models.fields.DateField')(null=True, blank=True)),
            ('death_latest_month_known', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('death_latest_day_known', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('birth_place', self.gf('django.db.models.fields.related.ForeignKey')(blank=True, related_name='people_official_birth_place', null=True, to=orm['places.Place'])),
            ('death_place', self.gf('django.db.models.fields.related.ForeignKey')(blank=True, related_name='people_official_death_place', null=True, to=orm['places.Place'])),
        ))
        db.send_create_signal('people', ['Official'])

        # Adding model 'Identity'
        db.create_table('people_identity', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('display_name', self.gf('django.db.models.fields.CharField')(max_length=200)),
            ('resident', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['people.Resident'], null=True, blank=True)),
        ))
        db.send_create_signal('people', ['Identity'])

        # Adding model 'NamePart'
        db.create_table('people_namepart', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('part', self.gf('django.db.models.fields.CharField')(max_length=100)),
            ('name_type', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['people.NameType'])),
            ('identity', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['people.Identity'])),
        ))
        db.send_create_signal('people', ['NamePart'])

        # Adding model 'Family'
        db.create_table('people_family', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('date_created', self.gf('django.db.models.fields.DateTimeField')(auto_now_add=True, blank=True)),
            ('date_modified', self.gf('django.db.models.fields.DateTimeField')(auto_now=True, blank=True)),
            ('display_name', self.gf('django.db.models.fields.CharField')(max_length=200)),
            ('description', self.gf('django.db.models.fields.TextField')(null=True, blank=True)),
        ))
        db.send_create_signal('people', ['Family'])

        # Adding M2M table for field members on 'Family'
        db.create_table('people_family_members', (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('family', models.ForeignKey(orm['people.family'], null=False)),
            ('resident', models.ForeignKey(orm['people.resident'], null=False))
        ))
        db.create_unique('people_family_members', ['family_id', 'resident_id'])

        # Adding model 'SeaVoyageGroup'
        db.create_table('people_seavoyagegroup', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('date_created', self.gf('django.db.models.fields.DateTimeField')(auto_now_add=True, blank=True)),
            ('date_modified', self.gf('django.db.models.fields.DateTimeField')(auto_now=True, blank=True)),
            ('display_name', self.gf('django.db.models.fields.CharField')(max_length=200)),
            ('description', self.gf('django.db.models.fields.TextField')(null=True, blank=True)),
            ('sea_voyage', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['events.SeaVoyage'], null=True, blank=True)),
        ))
        db.send_create_signal('people', ['SeaVoyageGroup'])

        # Adding M2M table for field members on 'SeaVoyageGroup'
        db.create_table('people_seavoyagegroup_members', (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('seavoyagegroup', models.ForeignKey(orm['people.seavoyagegroup'], null=False)),
            ('resident', models.ForeignKey(orm['people.resident'], null=False))
        ))
        db.create_unique('people_seavoyagegroup_members', ['seavoyagegroup_id', 'resident_id'])

        # Adding model 'Repository'
        db.create_table('people_repository', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('date_created', self.gf('django.db.models.fields.DateTimeField')(auto_now_add=True, blank=True)),
            ('date_modified', self.gf('django.db.models.fields.DateTimeField')(auto_now=True, blank=True)),
            ('display_name', self.gf('django.db.models.fields.CharField')(max_length=200)),
            ('description', self.gf('django.db.models.fields.TextField')(null=True, blank=True)),
        ))
        db.send_create_signal('people', ['Repository'])

        # Adding model 'Agency'
        db.create_table('people_agency', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('date_created', self.gf('django.db.models.fields.DateTimeField')(auto_now_add=True, blank=True)),
            ('date_modified', self.gf('django.db.models.fields.DateTimeField')(auto_now=True, blank=True)),
            ('display_name', self.gf('django.db.models.fields.CharField')(max_length=200)),
            ('description', self.gf('django.db.models.fields.TextField')(null=True, blank=True)),
        ))
        db.send_create_signal('people', ['Agency'])

        # Adding model 'LifeEvent'
        db.create_table('people_lifeevent', (
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
            ('identity', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['people.Identity'])),
            ('life_event_type', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['people.LifeEventType'])),
        ))
        db.send_create_signal('people', ['LifeEvent'])

        # Adding M2M table for field records on 'LifeEvent'
        db.create_table('people_lifeevent_records', (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('lifeevent', models.ForeignKey(orm['people.lifeevent'], null=False)),
            ('record', models.ForeignKey(orm['sources.record'], null=False))
        ))
        db.create_unique('people_lifeevent_records', ['lifeevent_id', 'record_id'])

        # Adding M2M table for field photographs on 'LifeEvent'
        db.create_table('people_lifeevent_photographs', (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('lifeevent', models.ForeignKey(orm['people.lifeevent'], null=False)),
            ('photograph', models.ForeignKey(orm['sources.photograph'], null=False))
        ))
        db.create_unique('people_lifeevent_photographs', ['lifeevent_id', 'photograph_id'])

        # Adding M2M table for field publications on 'LifeEvent'
        db.create_table('people_lifeevent_publications', (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('lifeevent', models.ForeignKey(orm['people.lifeevent'], null=False)),
            ('publication', models.ForeignKey(orm['sources.publication'], null=False))
        ))
        db.create_unique('people_lifeevent_publications', ['lifeevent_id', 'publication_id'])

        # Adding model 'LifePeriod'
        db.create_table('people_lifeperiod', (
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
            ('identity', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['people.Identity'])),
            ('life_period_type', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['people.LifePeriodType'])),
        ))
        db.send_create_signal('people', ['LifePeriod'])

        # Adding M2M table for field records on 'LifePeriod'
        db.create_table('people_lifeperiod_records', (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('lifeperiod', models.ForeignKey(orm['people.lifeperiod'], null=False)),
            ('record', models.ForeignKey(orm['sources.record'], null=False))
        ))
        db.create_unique('people_lifeperiod_records', ['lifeperiod_id', 'record_id'])

        # Adding M2M table for field photographs on 'LifePeriod'
        db.create_table('people_lifeperiod_photographs', (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('lifeperiod', models.ForeignKey(orm['people.lifeperiod'], null=False)),
            ('photograph', models.ForeignKey(orm['sources.photograph'], null=False))
        ))
        db.create_unique('people_lifeperiod_photographs', ['lifeperiod_id', 'photograph_id'])

        # Adding M2M table for field publications on 'LifePeriod'
        db.create_table('people_lifeperiod_publications', (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('lifeperiod', models.ForeignKey(orm['people.lifeperiod'], null=False)),
            ('publication', models.ForeignKey(orm['sources.publication'], null=False))
        ))
        db.create_unique('people_lifeperiod_publications', ['lifeperiod_id', 'publication_id'])

        # Adding model 'ResidentRelatedResident'
        db.create_table('people_residentrelatedresident', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('resident', self.gf('django.db.models.fields.related.ForeignKey')(related_name='main_resident', to=orm['people.Resident'])),
            ('related_resident', self.gf('django.db.models.fields.related.ForeignKey')(related_name='related_resident', to=orm['people.Resident'])),
            ('relationship', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['people.ResidentRelationship'])),
        ))
        db.send_create_signal('people', ['ResidentRelatedResident'])

        # Adding model 'LifeEventIdentity'
        db.create_table('people_lifeeventidentity', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('life_event', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['people.LifeEvent'])),
            ('identity', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['people.Identity'])),
            ('relationship', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['people.LifeEventIdentityRelationship'])),
        ))
        db.send_create_signal('people', ['LifeEventIdentity'])

        # Adding model 'LifePeriodEvent'
        db.create_table('people_lifeperiodevent', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('life_event', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['people.LifeEvent'])),
            ('life_period', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['people.LifePeriod'])),
            ('relationship', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['people.LifePeriodEventRelationship'])),
        ))
        db.send_create_signal('people', ['LifePeriodEvent'])

        # Adding model 'NameType'
        db.create_table('people_nametype', (
            ('rdftype_ptr', self.gf('django.db.models.fields.related.OneToOneField')(to=orm['linkeddata.RDFType'], unique=True, primary_key=True)),
        ))
        db.send_create_signal('people', ['NameType'])

        # Adding model 'LifeEventType'
        db.create_table('people_lifeeventtype', (
            ('rdftype_ptr', self.gf('django.db.models.fields.related.OneToOneField')(to=orm['linkeddata.RDFType'], unique=True, primary_key=True)),
        ))
        db.send_create_signal('people', ['LifeEventType'])

        # Adding model 'LifePeriodType'
        db.create_table('people_lifeperiodtype', (
            ('rdftype_ptr', self.gf('django.db.models.fields.related.OneToOneField')(to=orm['linkeddata.RDFType'], unique=True, primary_key=True)),
        ))
        db.send_create_signal('people', ['LifePeriodType'])

        # Adding model 'ResidentRelationship'
        db.create_table('people_residentrelationship', (
            ('rdfrelationship_ptr', self.gf('django.db.models.fields.related.OneToOneField')(to=orm['linkeddata.RDFRelationship'], unique=True, primary_key=True)),
        ))
        db.send_create_signal('people', ['ResidentRelationship'])

        # Adding model 'LifePeriodEventRelationship'
        db.create_table('people_lifeperiodeventrelationship', (
            ('rdfrelationship_ptr', self.gf('django.db.models.fields.related.OneToOneField')(to=orm['linkeddata.RDFRelationship'], unique=True, primary_key=True)),
        ))
        db.send_create_signal('people', ['LifePeriodEventRelationship'])

        # Adding model 'LifeEventIdentityRelationship'
        db.create_table('people_lifeeventidentityrelationship', (
            ('rdfrelationship_ptr', self.gf('django.db.models.fields.related.OneToOneField')(to=orm['linkeddata.RDFRelationship'], unique=True, primary_key=True)),
        ))
        db.send_create_signal('people', ['LifeEventIdentityRelationship'])


    def backwards(self, orm):
        # Deleting model 'Resident'
        db.delete_table('people_resident')

        # Deleting model 'Official'
        db.delete_table('people_official')

        # Deleting model 'Identity'
        db.delete_table('people_identity')

        # Deleting model 'NamePart'
        db.delete_table('people_namepart')

        # Deleting model 'Family'
        db.delete_table('people_family')

        # Removing M2M table for field members on 'Family'
        db.delete_table('people_family_members')

        # Deleting model 'SeaVoyageGroup'
        db.delete_table('people_seavoyagegroup')

        # Removing M2M table for field members on 'SeaVoyageGroup'
        db.delete_table('people_seavoyagegroup_members')

        # Deleting model 'Repository'
        db.delete_table('people_repository')

        # Deleting model 'Agency'
        db.delete_table('people_agency')

        # Deleting model 'LifeEvent'
        db.delete_table('people_lifeevent')

        # Removing M2M table for field records on 'LifeEvent'
        db.delete_table('people_lifeevent_records')

        # Removing M2M table for field photographs on 'LifeEvent'
        db.delete_table('people_lifeevent_photographs')

        # Removing M2M table for field publications on 'LifeEvent'
        db.delete_table('people_lifeevent_publications')

        # Deleting model 'LifePeriod'
        db.delete_table('people_lifeperiod')

        # Removing M2M table for field records on 'LifePeriod'
        db.delete_table('people_lifeperiod_records')

        # Removing M2M table for field photographs on 'LifePeriod'
        db.delete_table('people_lifeperiod_photographs')

        # Removing M2M table for field publications on 'LifePeriod'
        db.delete_table('people_lifeperiod_publications')

        # Deleting model 'ResidentRelatedResident'
        db.delete_table('people_residentrelatedresident')

        # Deleting model 'LifeEventIdentity'
        db.delete_table('people_lifeeventidentity')

        # Deleting model 'LifePeriodEvent'
        db.delete_table('people_lifeperiodevent')

        # Deleting model 'NameType'
        db.delete_table('people_nametype')

        # Deleting model 'LifeEventType'
        db.delete_table('people_lifeeventtype')

        # Deleting model 'LifePeriodType'
        db.delete_table('people_lifeperiodtype')

        # Deleting model 'ResidentRelationship'
        db.delete_table('people_residentrelationship')

        # Deleting model 'LifePeriodEventRelationship'
        db.delete_table('people_lifeperiodeventrelationship')

        # Deleting model 'LifeEventIdentityRelationship'
        db.delete_table('people_lifeeventidentityrelationship')


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
        'people.family': {
            'Meta': {'object_name': 'Family'},
            'date_created': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'date_modified': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'}),
            'description': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'display_name': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'members': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['people.Resident']", 'symmetrical': 'False'})
        },
        'people.identity': {
            'Meta': {'object_name': 'Identity'},
            'display_name': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'resident': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['people.Resident']", 'null': 'True', 'blank': 'True'})
        },
        'people.lifeevent': {
            'Meta': {'object_name': 'LifeEvent'},
            'date_created': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'date_modified': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'}),
            'description': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'end_earliest_date': ('django.db.models.fields.DateField', [], {'null': 'True', 'blank': 'True'}),
            'end_earliest_day_known': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'end_earliest_month_known': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'end_latest_date': ('django.db.models.fields.DateField', [], {'null': 'True', 'blank': 'True'}),
            'end_latest_day_known': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'end_latest_month_known': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'identity': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['people.Identity']"}),
            'label': ('django.db.models.fields.CharField', [], {'max_length': '250', 'null': 'True', 'blank': 'True'}),
            'life_event_type': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['people.LifeEventType']"}),
            'photographs': ('django.db.models.fields.related.ManyToManyField', [], {'symmetrical': 'False', 'to': "orm['sources.Photograph']", 'null': 'True', 'blank': 'True'}),
            'publications': ('django.db.models.fields.related.ManyToManyField', [], {'symmetrical': 'False', 'to': "orm['sources.Publication']", 'null': 'True', 'blank': 'True'}),
            'records': ('django.db.models.fields.related.ManyToManyField', [], {'symmetrical': 'False', 'to': "orm['sources.Record']", 'null': 'True', 'blank': 'True'}),
            'related_identities': ('django.db.models.fields.related.ManyToManyField', [], {'related_name': "'related_identities'", 'to': "orm['people.Identity']", 'through': "orm['people.LifeEventIdentity']", 'blank': 'True', 'symmetrical': 'False', 'null': 'True'}),
            'start_earliest_date': ('django.db.models.fields.DateField', [], {'null': 'True', 'blank': 'True'}),
            'start_earliest_day_known': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'start_earliest_month_known': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'start_latest_date': ('django.db.models.fields.DateField', [], {'null': 'True', 'blank': 'True'}),
            'start_latest_day_known': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'start_latest_month_known': ('django.db.models.fields.BooleanField', [], {'default': 'False'})
        },
        'people.lifeeventidentity': {
            'Meta': {'object_name': 'LifeEventIdentity'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'identity': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['people.Identity']"}),
            'life_event': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['people.LifeEvent']"}),
            'relationship': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['people.LifeEventIdentityRelationship']"})
        },
        'people.lifeeventidentityrelationship': {
            'Meta': {'object_name': 'LifeEventIdentityRelationship', '_ormbases': ['linkeddata.RDFRelationship']},
            'rdfrelationship_ptr': ('django.db.models.fields.related.OneToOneField', [], {'to': "orm['linkeddata.RDFRelationship']", 'unique': 'True', 'primary_key': 'True'})
        },
        'people.lifeeventtype': {
            'Meta': {'object_name': 'LifeEventType', '_ormbases': ['linkeddata.RDFType']},
            'rdftype_ptr': ('django.db.models.fields.related.OneToOneField', [], {'to': "orm['linkeddata.RDFType']", 'unique': 'True', 'primary_key': 'True'})
        },
        'people.lifeperiod': {
            'Meta': {'object_name': 'LifePeriod'},
            'date_created': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'date_modified': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'}),
            'description': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'end_earliest_date': ('django.db.models.fields.DateField', [], {'null': 'True', 'blank': 'True'}),
            'end_earliest_day_known': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'end_earliest_month_known': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'end_latest_date': ('django.db.models.fields.DateField', [], {'null': 'True', 'blank': 'True'}),
            'end_latest_day_known': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'end_latest_month_known': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'identity': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['people.Identity']"}),
            'label': ('django.db.models.fields.CharField', [], {'max_length': '250', 'null': 'True', 'blank': 'True'}),
            'life_period_type': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['people.LifePeriodType']"}),
            'photographs': ('django.db.models.fields.related.ManyToManyField', [], {'symmetrical': 'False', 'to': "orm['sources.Photograph']", 'null': 'True', 'blank': 'True'}),
            'publications': ('django.db.models.fields.related.ManyToManyField', [], {'symmetrical': 'False', 'to': "orm['sources.Publication']", 'null': 'True', 'blank': 'True'}),
            'records': ('django.db.models.fields.related.ManyToManyField', [], {'symmetrical': 'False', 'to': "orm['sources.Record']", 'null': 'True', 'blank': 'True'}),
            'related_life_event': ('django.db.models.fields.related.ManyToManyField', [], {'symmetrical': 'False', 'to': "orm['people.LifeEvent']", 'null': 'True', 'through': "orm['people.LifePeriodEvent']", 'blank': 'True'}),
            'start_earliest_date': ('django.db.models.fields.DateField', [], {'null': 'True', 'blank': 'True'}),
            'start_earliest_day_known': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'start_earliest_month_known': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'start_latest_date': ('django.db.models.fields.DateField', [], {'null': 'True', 'blank': 'True'}),
            'start_latest_day_known': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'start_latest_month_known': ('django.db.models.fields.BooleanField', [], {'default': 'False'})
        },
        'people.lifeperiodevent': {
            'Meta': {'object_name': 'LifePeriodEvent'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'life_event': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['people.LifeEvent']"}),
            'life_period': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['people.LifePeriod']"}),
            'relationship': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['people.LifePeriodEventRelationship']"})
        },
        'people.lifeperiodeventrelationship': {
            'Meta': {'object_name': 'LifePeriodEventRelationship', '_ormbases': ['linkeddata.RDFRelationship']},
            'rdfrelationship_ptr': ('django.db.models.fields.related.OneToOneField', [], {'to': "orm['linkeddata.RDFRelationship']", 'unique': 'True', 'primary_key': 'True'})
        },
        'people.lifeperiodtype': {
            'Meta': {'object_name': 'LifePeriodType', '_ormbases': ['linkeddata.RDFType']},
            'rdftype_ptr': ('django.db.models.fields.related.OneToOneField', [], {'to': "orm['linkeddata.RDFType']", 'unique': 'True', 'primary_key': 'True'})
        },
        'people.namepart': {
            'Meta': {'object_name': 'NamePart'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'identity': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['people.Identity']"}),
            'name_type': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['people.NameType']"}),
            'part': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        },
        'people.nametype': {
            'Meta': {'object_name': 'NameType', '_ormbases': ['linkeddata.RDFType']},
            'rdftype_ptr': ('django.db.models.fields.related.OneToOneField', [], {'to': "orm['linkeddata.RDFType']", 'unique': 'True', 'primary_key': 'True'})
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
        'people.seavoyagegroup': {
            'Meta': {'object_name': 'SeaVoyageGroup'},
            'date_created': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'date_modified': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'}),
            'description': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'display_name': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'members': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['people.Resident']", 'symmetrical': 'False'}),
            'sea_voyage': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['events.SeaVoyage']", 'null': 'True', 'blank': 'True'})
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
        'sources.aggregationtype': {
            'Meta': {'object_name': 'AggregationType', '_ormbases': ['linkeddata.RDFType']},
            'rdftype_ptr': ('django.db.models.fields.related.OneToOneField', [], {'to': "orm['linkeddata.RDFType']", 'unique': 'True', 'primary_key': 'True'})
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
        'things.ship': {
            'Meta': {'object_name': 'Ship'},
            'date_created': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'date_modified': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'}),
            'description': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'label': ('django.db.models.fields.CharField', [], {'max_length': '250', 'null': 'True', 'blank': 'True'})
        }
    }

    complete_apps = ['people']