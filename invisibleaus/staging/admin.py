from django.contrib import admin

from invisibleaus.staging.models import *


class NSWBDMAdmin(admin.ModelAdmin):
    ordering = ('registration_year', 'registration_number')
    list_display = (
                    'highlight_duplicates',
                    'surname',
                    'given_names',
                    'event_type',
                    'father_spouse_surname',
                    'mother_spouses_names',
                    'registration_place',
                    'volume_reference',
                    'registration_year',
                    'registration_number'
                    )
    list_editable = (
                    'surname',
                    'given_names',
                    'event_type',
                    'father_spouse_surname',
                    'mother_spouses_names',
                    'registration_place',
                    )


admin.site.register(NSWBDMRegister, NSWBDMAdmin)
