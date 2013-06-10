#!/usr/bin/env python

from django.contrib import admin
from invisibleaus.people.models import *
from invisibleaus.sources.models import *


class RelatedRecordInline(admin.TabularInline):
    model = ResidentRelatedRecord


class ResidentAdmin(admin.ModelAdmin):
    inlines = [
        RelatedRecordInline,
    ]


class RecordAdmin(admin.ModelAdmin):
    inlines = [
        RelatedRecordInline,
    ]

#admin.site.register(Resident, ResidentAdmin)
#admin.site.register(Record, RecordAdmin)
