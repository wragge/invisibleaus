#!/usr/bin/env python

from django.contrib import admin
from invisibleaus.people.models import *
from invisibleaus.sources.models import *

from rstools.retrieve import RSSeriesClient, RSItemClient


class RelatedRecordInline(admin.TabularInline):
    model = ResidentRelatedRecord
    extra = 1


class ResidentAltNameInline(admin.TabularInline):
    model = ResidentAltName
    extra = 1


class ResidentInline(admin.TabularInline):
    model = ResidentRelatedResident
    extra = 1
    fk_name = 'related_resident'


class ResidentNamePartInline(admin.TabularInline):
    model = ResidentNamePart
    extra = 1


class ResidentAdmin(admin.ModelAdmin):
    inlines = [
        ResidentAltNameInline,
        RelatedRecordInline,
        ResidentInline
    ]
    fieldsets = (
        (None, {
            'fields': (
                'display_name',
                'biography',
                'papertrails'
            )
        }),
        ('Birth', {
            'classes': ('collapse',),
            'fields': (
                'birth_earliest_date',
                'birth_earliest_month_known',
                'birth_earliest_day_known',
                'birth_place'
            )
        }),
        ('Birth (latest possible date)', {
            'classes': ('collapse',),
            'fields': (
                'birth_latest_date',
                'birth_latest_month_known',
                'birth_latest_day_known',
            )
        }),
        ('Death', {
            'classes': ('collapse',),
            'fields': (
                'death_earliest_date',
                'death_earliest_month_known',
                'death_earliest_day_known',
                'death_place'
            )
        }),
        ('Death (latest possible date)', {
            'classes': ('collapse',),
            'fields': (
                'death_latest_date',
                'death_latest_month_known',
                'death_latest_day_known',
            )
        }),
    )
    list_display = (
        'display_name',
        'birth_earliest_date',
        'papertrails'
    )
    list_editable = (
        'papertrails',
    )


class ResidentAltNameAdmin(admin.ModelAdmin):
    inlines = [
        ResidentNamePartInline
    ]


class RecordAdmin(admin.ModelAdmin):
    inlines = [
        RelatedRecordInline,
    ]

    def save_model(self, request, obj, form, change):
        if not change and obj.numeric_identifier and not obj.title:
            barcode = obj.numeric_identifier
            print barcode
            rs = RSItemClient()
            rsseries = RSSeriesClient()
            item_details = rs.get_summary(barcode)
            dates = item_details['contents_dates']
            citation = '{}, {}'.format(
                item_details['series'],
                item_details['control_symbol']
            )
            series_details = rsseries.get_summary(item_details['series'])
            repository = Repository.objects.get(display_name='National Archives of Australia')
            series_type, created = RecordType.objects.get_or_create(label='series')
            series, created = Record.objects.get_or_create(
                identifier=item_details['series'],
                record_type=series_type,
                repository=repository,
                defaults={
                    'title': series_details['title']
                }

            )
            item_type, created = RecordType.objects.get_or_create(label='item')
            obj.is_part_of = series
            obj.record_type = item_type
            obj.identifier = item_details['control_symbol']
            obj.title = item_details['title']
            obj.date_string = dates['date_str']
            obj.start_date = dates['start_date']['date']
            obj.start_month_known = dates['start_date']['month']
            obj.start_day_known = dates['start_date']['day']
            obj.end_date = dates['end_date']['date']
            obj.end_month_known = dates['end_date']['month']
            obj.end_day_known = dates['end_date']['day']
            obj.access_status = item_details['access_status']
            obj.short_citation = citation
            obj.repository = repository
            obj.number_of_items = int(item_details['digitised_pages'])
            obj.save()


admin.site.register(Resident, ResidentAdmin)
admin.site.register(ResidentAltName, ResidentAltNameAdmin)
admin.site.register(Record, RecordAdmin)
admin.site.register(ResidentRecordRelationship)
admin.site.register(ResidentRelationship)
