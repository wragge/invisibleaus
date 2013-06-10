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

        # Adding model 'ResidentAltName'
        db.create_table('people_residentaltname', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('display_name', self.gf('django.db.models.fields.CharField')(max_length=200)),
            ('note', self.gf('django.db.models.fields.TextField')(null=True, blank=True)),
            ('name_type', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['people.NameType'], null=True, blank=True)),
            ('resident', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['people.Resident'])),
        ))
        db.send_create_signal('people', ['ResidentAltName'])

        # Adding model 'ResidentNamePart'
        db.create_table('people_residentnamepart', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('part', self.gf('django.db.models.fields.CharField')(max_length=100)),
            ('name_part_type', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['people.NamePartType'], null=True, blank=True)),
            ('alt_name', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['people.ResidentAltName'])),
        ))
        db.send_create_signal('people', ['ResidentNamePart'])

        # Adding model 'IdentityAltName'
        db.create_table('people_identityaltname', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('display_name', self.gf('django.db.models.fields.CharField')(max_length=200)),
            ('note', self.gf('django.db.models.fields.TextField')(null=True, blank=True)),
            ('name_type', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['people.NameType'], null=True, blank=True)),
            ('identity', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['people.Identity'])),
        ))
        db.send_create_signal('people', ['IdentityAltName'])

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
            ('identifier', self.gf('django.db.models.fields.CharField')(max_length=20, null=True, blank=True)),
        ))
        db.send_create_signal('people', ['Agency'])

        # Adding model 'AgencyRelatedAgency'
        db.create_table('people_agencyrelatedagency', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('main_agency', self.gf('django.db.models.fields.related.ForeignKey')(related_name='main_agency', to=orm['people.Agency'])),
            ('related_agency', self.gf('django.db.models.fields.related.ForeignKey')(related_name='related_agency', to=orm['people.Agency'])),
            ('relationship', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['people.AgencyRelationship'])),
        ))
        db.send_create_signal('people', ['AgencyRelatedAgency'])

        # Adding model 'AgencyRelatedRecord'
        db.create_table('people_agencyrelatedrecord', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('record', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['sources.Record'])),
            ('agency', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['people.Agency'])),
            ('relationship', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['people.AgencyRecordRelationship'])),
            ('date_string', self.gf('django.db.models.fields.CharField')(max_length=50, blank=True)),
            ('start_date', self.gf('django.db.models.fields.DateField')(null=True, blank=True)),
            ('start_month_known', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('start_day_known', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('end_date', self.gf('django.db.models.fields.DateField')(null=True, blank=True)),
            ('end_month_known', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('end_day_known', self.gf('django.db.models.fields.BooleanField')(default=False)),
        ))
        db.send_create_signal('people', ['AgencyRelatedRecord'])

        # Adding model 'AgencyRecordRelationship'
        db.create_table('people_agencyrecordrelationship', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('label', self.gf('django.db.models.fields.CharField')(max_length=50)),
        ))
        db.send_create_signal('people', ['AgencyRecordRelationship'])

        # Adding M2M table for field rdf_property on 'AgencyRecordRelationship'
        db.create_table('people_agencyrecordrelationship_rdf_property', (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('agencyrecordrelationship', models.ForeignKey(orm['people.agencyrecordrelationship'], null=False)),
            ('rdfproperty', models.ForeignKey(orm['linkeddata.rdfproperty'], null=False))
        ))
        db.create_unique('people_agencyrecordrelationship_rdf_property', ['agencyrecordrelationship_id', 'rdfproperty_id'])

        # Adding model 'AgencyRelationship'
        db.create_table('people_agencyrelationship', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('label', self.gf('django.db.models.fields.CharField')(max_length=50)),
        ))
        db.send_create_signal('people', ['AgencyRelationship'])

        # Adding M2M table for field rdf_property on 'AgencyRelationship'
        db.create_table('people_agencyrelationship_rdf_property', (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('agencyrelationship', models.ForeignKey(orm['people.agencyrelationship'], null=False)),
            ('rdfproperty', models.ForeignKey(orm['linkeddata.rdfproperty'], null=False))
        ))
        db.create_unique('people_agencyrelationship_rdf_property', ['agencyrelationship_id', 'rdfproperty_id'])

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

        # Adding model 'ResidentRelatedRecord'
        db.create_table('people_residentrelatedrecord', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('resident', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['people.Resident'])),
            ('record', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['sources.Record'])),
            ('relationship', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['people.ResidentRecordRelationship'])),
        ))
        db.send_create_signal('people', ['ResidentRelatedRecord'])

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
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('label', self.gf('django.db.models.fields.CharField')(max_length=50)),
        ))
        db.send_create_signal('people', ['NameType'])

        # Adding M2M table for field rdf_class on 'NameType'
        db.create_table('people_nametype_rdf_class', (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('nametype', models.ForeignKey(orm['people.nametype'], null=False)),
            ('rdfclass', models.ForeignKey(orm['linkeddata.rdfclass'], null=False))
        ))
        db.create_unique('people_nametype_rdf_class', ['nametype_id', 'rdfclass_id'])

        # Adding model 'NamePartType'
        db.create_table('people_nameparttype', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('label', self.gf('django.db.models.fields.CharField')(max_length=50)),
        ))
        db.send_create_signal('people', ['NamePartType'])

        # Adding M2M table for field rdf_class on 'NamePartType'
        db.create_table('people_nameparttype_rdf_class', (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('nameparttype', models.ForeignKey(orm['people.nameparttype'], null=False)),
            ('rdfclass', models.ForeignKey(orm['linkeddata.rdfclass'], null=False))
        ))
        db.create_unique('people_nameparttype_rdf_class', ['nameparttype_id', 'rdfclass_id'])

        # Adding model 'LifeEventType'
        db.create_table('people_lifeeventtype', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('label', self.gf('django.db.models.fields.CharField')(max_length=50)),
        ))
        db.send_create_signal('people', ['LifeEventType'])

        # Adding M2M table for field rdf_class on 'LifeEventType'
        db.create_table('people_lifeeventtype_rdf_class', (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('lifeeventtype', models.ForeignKey(orm['people.lifeeventtype'], null=False)),
            ('rdfclass', models.ForeignKey(orm['linkeddata.rdfclass'], null=False))
        ))
        db.create_unique('people_lifeeventtype_rdf_class', ['lifeeventtype_id', 'rdfclass_id'])

        # Adding model 'LifePeriodType'
        db.create_table('people_lifeperiodtype', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('label', self.gf('django.db.models.fields.CharField')(max_length=50)),
        ))
        db.send_create_signal('people', ['LifePeriodType'])

        # Adding M2M table for field rdf_class on 'LifePeriodType'
        db.create_table('people_lifeperiodtype_rdf_class', (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('lifeperiodtype', models.ForeignKey(orm['people.lifeperiodtype'], null=False)),
            ('rdfclass', models.ForeignKey(orm['linkeddata.rdfclass'], null=False))
        ))
        db.create_unique('people_lifeperiodtype_rdf_class', ['lifeperiodtype_id', 'rdfclass_id'])

        # Adding model 'ResidentRelationship'
        db.create_table('people_residentrelationship', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('label', self.gf('django.db.models.fields.CharField')(max_length=50)),
        ))
        db.send_create_signal('people', ['ResidentRelationship'])

        # Adding M2M table for field rdf_property on 'ResidentRelationship'
        db.create_table('people_residentrelationship_rdf_property', (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('residentrelationship', models.ForeignKey(orm['people.residentrelationship'], null=False)),
            ('rdfproperty', models.ForeignKey(orm['linkeddata.rdfproperty'], null=False))
        ))
        db.create_unique('people_residentrelationship_rdf_property', ['residentrelationship_id', 'rdfproperty_id'])

        # Adding model 'ResidentRecordRelationship'
        db.create_table('people_residentrecordrelationship', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('label', self.gf('django.db.models.fields.CharField')(max_length=50)),
        ))
        db.send_create_signal('people', ['ResidentRecordRelationship'])

        # Adding M2M table for field rdf_property on 'ResidentRecordRelationship'
        db.create_table('people_residentrecordrelationship_rdf_property', (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('residentrecordrelationship', models.ForeignKey(orm['people.residentrecordrelationship'], null=False)),
            ('rdfproperty', models.ForeignKey(orm['linkeddata.rdfproperty'], null=False))
        ))
        db.create_unique('people_residentrecordrelationship_rdf_property', ['residentrecordrelationship_id', 'rdfproperty_id'])

        # Adding model 'LifePeriodEventRelationship'
        db.create_table('people_lifeperiodeventrelationship', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('label', self.gf('django.db.models.fields.CharField')(max_length=50)),
        ))
        db.send_create_signal('people', ['LifePeriodEventRelationship'])

        # Adding M2M table for field rdf_property on 'LifePeriodEventRelationship'
        db.create_table('people_lifeperiodeventrelationship_rdf_property', (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('lifeperiodeventrelationship', models.ForeignKey(orm['people.lifeperiodeventrelationship'], null=False)),
            ('rdfproperty', models.ForeignKey(orm['linkeddata.rdfproperty'], null=False))
        ))
        db.create_unique('people_lifeperiodeventrelationship_rdf_property', ['lifeperiodeventrelationship_id', 'rdfproperty_id'])

        # Adding model 'LifeEventIdentityRelationship'
        db.create_table('people_lifeeventidentityrelationship', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('label', self.gf('django.db.models.fields.CharField')(max_length=50)),
        ))
        db.send_create_signal('people', ['LifeEventIdentityRelationship'])

        # Adding M2M table for field rdf_property on 'LifeEventIdentityRelationship'
        db.create_table('people_lifeeventidentityrelationship_rdf_property', (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('lifeeventidentityrelationship', models.ForeignKey(orm['people.lifeeventidentityrelationship'], null=False)),
            ('rdfproperty', models.ForeignKey(orm['linkeddata.rdfproperty'], null=False))
        ))
        db.create_unique('people_lifeeventidentityrelationship_rdf_property', ['lifeeventidentityrelationship_id', 'rdfproperty_id'])


    def backwards(self, orm):
        # Deleting model 'Resident'
        db.delete_table('people_resident')

        # Deleting model 'Official'
        db.delete_table('people_official')

        # Deleting model 'Identity'
        db.delete_table('people_identity')

        # Deleting model 'ResidentAltName'
        db.delete_table('people_residentaltname')

        # Deleting model 'ResidentNamePart'
        db.delete_table('people_residentnamepart')

        # Deleting model 'IdentityAltName'
        db.delete_table('people_identityaltname')

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

        # Deleting model 'AgencyRelatedAgency'
        db.delete_table('people_agencyrelatedagency')

        # Deleting model 'AgencyRelatedRecord'
        db.delete_table('people_agencyrelatedrecord')

        # Deleting model 'AgencyRecordRelationship'
        db.delete_table('people_agencyrecordrelationship')

        # Removing M2M table for field rdf_property on 'AgencyRecordRelationship'
        db.delete_table('people_agencyrecordrelationship_rdf_property')

        # Deleting model 'AgencyRelationship'
        db.delete_table('people_agencyrelationship')

        # Removing M2M table for field rdf_property on 'AgencyRelationship'
        db.delete_table('people_agencyrelationship_rdf_property')

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

        # Deleting model 'ResidentRelatedRecord'
        db.delete_table('people_residentrelatedrecord')

        # Deleting model 'ResidentRelatedResident'
        db.delete_table('people_residentrelatedresident')

        # Deleting model 'LifeEventIdentity'
        db.delete_table('people_lifeeventidentity')

        # Deleting model 'LifePeriodEvent'
        db.delete_table('people_lifeperiodevent')

        # Deleting model 'NameType'
        db.delete_table('people_nametype')

        # Removing M2M table for field rdf_class on 'NameType'
        db.delete_table('people_nametype_rdf_class')

        # Deleting model 'NamePartType'
        db.delete_table('people_nameparttype')

        # Removing M2M table for field rdf_class on 'NamePartType'
        db.delete_table('people_nameparttype_rdf_class')

        # Deleting model 'LifeEventType'
        db.delete_table('people_lifeeventtype')

        # Removing M2M table for field rdf_class on 'LifeEventType'
        db.delete_table('people_lifeeventtype_rdf_class')

        # Deleting model 'LifePeriodType'
        db.delete_table('people_lifeperiodtype')

        # Removing M2M table for field rdf_class on 'LifePeriodType'
        db.delete_table('people_lifeperiodtype_rdf_class')

        # Deleting model 'ResidentRelationship'
        db.delete_table('people_residentrelationship')

        # Removing M2M table for field rdf_property on 'ResidentRelationship'
        db.delete_table('people_residentrelationship_rdf_property')

        # Deleting model 'ResidentRecordRelationship'
        db.delete_table('people_residentrecordrelationship')

        # Removing M2M table for field rdf_property on 'ResidentRecordRelationship'
        db.delete_table('people_residentrecordrelationship_rdf_property')

        # Deleting model 'LifePeriodEventRelationship'
        db.delete_table('people_lifeperiodeventrelationship')

        # Removing M2M table for field rdf_property on 'LifePeriodEventRelationship'
        db.delete_table('people_lifeperiodeventrelationship_rdf_property')

        # Deleting model 'LifeEventIdentityRelationship'
        db.delete_table('people_lifeeventidentityrelationship')

        # Removing M2M table for field rdf_property on 'LifeEventIdentityRelationship'
        db.delete_table('people_lifeeventidentityrelationship_rdf_property')


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
        'linkeddata.rdfschema': {
            'Meta': {'object_name': 'RDFSchema'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'prefix': ('django.db.models.fields.CharField', [], {'max_length': '20'}),
            'uri': ('django.db.models.fields.CharField', [], {'max_length': '200'})
        },
        'people.agency': {
            'Meta': {'object_name': 'Agency'},
            'date_created': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'date_modified': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'}),
            'description': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'display_name': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'identifier': ('django.db.models.fields.CharField', [], {'max_length': '20', 'null': 'True', 'blank': 'True'}),
            'related_agencies': ('django.db.models.fields.related.ManyToManyField', [], {'symmetrical': 'False', 'to': "orm['people.Agency']", 'null': 'True', 'through': "orm['people.AgencyRelatedAgency']", 'blank': 'True'}),
            'related_records': ('django.db.models.fields.related.ManyToManyField', [], {'symmetrical': 'False', 'to': "orm['sources.Record']", 'null': 'True', 'through': "orm['people.AgencyRelatedRecord']", 'blank': 'True'})
        },
        'people.agencyrecordrelationship': {
            'Meta': {'object_name': 'AgencyRecordRelationship'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'label': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'rdf_property': ('django.db.models.fields.related.ManyToManyField', [], {'symmetrical': 'False', 'to': "orm['linkeddata.RDFProperty']", 'null': 'True', 'blank': 'True'})
        },
        'people.agencyrelatedagency': {
            'Meta': {'object_name': 'AgencyRelatedAgency'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'main_agency': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'main_agency'", 'to': "orm['people.Agency']"}),
            'related_agency': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'related_agency'", 'to': "orm['people.Agency']"}),
            'relationship': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['people.AgencyRelationship']"})
        },
        'people.agencyrelatedrecord': {
            'Meta': {'object_name': 'AgencyRelatedRecord'},
            'agency': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['people.Agency']"}),
            'date_string': ('django.db.models.fields.CharField', [], {'max_length': '50', 'blank': 'True'}),
            'end_date': ('django.db.models.fields.DateField', [], {'null': 'True', 'blank': 'True'}),
            'end_day_known': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'end_month_known': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'record': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['sources.Record']"}),
            'relationship': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['people.AgencyRecordRelationship']"}),
            'start_date': ('django.db.models.fields.DateField', [], {'null': 'True', 'blank': 'True'}),
            'start_day_known': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'start_month_known': ('django.db.models.fields.BooleanField', [], {'default': 'False'})
        },
        'people.agencyrelationship': {
            'Meta': {'object_name': 'AgencyRelationship'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'label': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'rdf_property': ('django.db.models.fields.related.ManyToManyField', [], {'symmetrical': 'False', 'to': "orm['linkeddata.RDFProperty']", 'null': 'True', 'blank': 'True'})
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
        'people.identityaltname': {
            'Meta': {'object_name': 'IdentityAltName'},
            'display_name': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'identity': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['people.Identity']"}),
            'name_type': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['people.NameType']", 'null': 'True', 'blank': 'True'}),
            'note': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'})
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
            'Meta': {'object_name': 'LifeEventIdentityRelationship'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'label': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'rdf_property': ('django.db.models.fields.related.ManyToManyField', [], {'symmetrical': 'False', 'to': "orm['linkeddata.RDFProperty']", 'null': 'True', 'blank': 'True'})
        },
        'people.lifeeventtype': {
            'Meta': {'object_name': 'LifeEventType'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'label': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'rdf_class': ('django.db.models.fields.related.ManyToManyField', [], {'symmetrical': 'False', 'to': "orm['linkeddata.RDFClass']", 'null': 'True', 'blank': 'True'})
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
            'Meta': {'object_name': 'LifePeriodEventRelationship'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'label': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'rdf_property': ('django.db.models.fields.related.ManyToManyField', [], {'symmetrical': 'False', 'to': "orm['linkeddata.RDFProperty']", 'null': 'True', 'blank': 'True'})
        },
        'people.lifeperiodtype': {
            'Meta': {'object_name': 'LifePeriodType'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'label': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'rdf_class': ('django.db.models.fields.related.ManyToManyField', [], {'symmetrical': 'False', 'to': "orm['linkeddata.RDFClass']", 'null': 'True', 'blank': 'True'})
        },
        'people.nameparttype': {
            'Meta': {'object_name': 'NamePartType'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'label': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'rdf_class': ('django.db.models.fields.related.ManyToManyField', [], {'symmetrical': 'False', 'to': "orm['linkeddata.RDFClass']", 'null': 'True', 'blank': 'True'})
        },
        'people.nametype': {
            'Meta': {'object_name': 'NameType'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'label': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'rdf_class': ('django.db.models.fields.related.ManyToManyField', [], {'symmetrical': 'False', 'to': "orm['linkeddata.RDFClass']", 'null': 'True', 'blank': 'True'})
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
            'related_records': ('django.db.models.fields.related.ManyToManyField', [], {'symmetrical': 'False', 'to': "orm['sources.Record']", 'null': 'True', 'through': "orm['people.ResidentRelatedRecord']", 'blank': 'True'}),
            'related_residents': ('django.db.models.fields.related.ManyToManyField', [], {'symmetrical': 'False', 'to': "orm['people.Resident']", 'null': 'True', 'through': "orm['people.ResidentRelatedResident']", 'blank': 'True'})
        },
        'people.residentaltname': {
            'Meta': {'object_name': 'ResidentAltName'},
            'display_name': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name_type': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['people.NameType']", 'null': 'True', 'blank': 'True'}),
            'note': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'resident': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['people.Resident']"})
        },
        'people.residentnamepart': {
            'Meta': {'object_name': 'ResidentNamePart'},
            'alt_name': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['people.ResidentAltName']"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name_part_type': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['people.NamePartType']", 'null': 'True', 'blank': 'True'}),
            'part': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        },
        'people.residentrecordrelationship': {
            'Meta': {'object_name': 'ResidentRecordRelationship'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'label': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'rdf_property': ('django.db.models.fields.related.ManyToManyField', [], {'symmetrical': 'False', 'to': "orm['linkeddata.RDFProperty']", 'null': 'True', 'blank': 'True'})
        },
        'people.residentrelatedrecord': {
            'Meta': {'object_name': 'ResidentRelatedRecord'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'record': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['sources.Record']"}),
            'relationship': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['people.ResidentRecordRelationship']"}),
            'resident': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['people.Resident']"})
        },
        'people.residentrelatedresident': {
            'Meta': {'object_name': 'ResidentRelatedResident'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'related_resident': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'related_resident'", 'to': "orm['people.Resident']"}),
            'relationship': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['people.ResidentRelationship']"}),
            'resident': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'main_resident'", 'to': "orm['people.Resident']"})
        },
        'people.residentrelationship': {
            'Meta': {'object_name': 'ResidentRelationship'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'label': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'rdf_property': ('django.db.models.fields.related.ManyToManyField', [], {'symmetrical': 'False', 'to': "orm['linkeddata.RDFProperty']", 'null': 'True', 'blank': 'True'})
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
            'Meta': {'object_name': 'PlaceRelationship'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'label': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'rdf_property': ('django.db.models.fields.related.ManyToManyField', [], {'symmetrical': 'False', 'to': "orm['linkeddata.RDFProperty']", 'null': 'True', 'blank': 'True'})
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
        'sources.recordtype': {
            'Meta': {'object_name': 'RecordType'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'label': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'rdf_class': ('django.db.models.fields.related.ManyToManyField', [], {'symmetrical': 'False', 'to': "orm['linkeddata.RDFClass']", 'null': 'True', 'blank': 'True'})
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