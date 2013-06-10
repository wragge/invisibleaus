from django import forms
from django.forms import ModelForm
from django.forms.extras.widgets import SelectDateWidget
from calendar import monthrange

from invisibleaus.people.models import *
from invisibleaus.sources.models import *

from rstools.retrieve import RSSeriesClient, RSItemClient

YEARS = [year for year in range(1800, 1960)]


class NewSelectDateWidget(SelectDateWidget):
    none_value = (0, 'unknown')


class DateSelectMixin(object):
    def clean_date(self, date, type):
        if date:
            year, month, day = date.split('-')
            if int(month) == 0:
                if type == 'start':
                    month = '1'
                    day = '1'
                elif type == 'end':
                    month = '12'
                    day = '31'
            else:
                if int(day) == 0:
                    if type == 'start':
                        day = '1'
                    elif type == 'end':
                        day = monthrange(int(year), int(month))[1]
            date = '%s-%s-%s' % (year, month, day)
        else:
            date = None
        return date

    def clean_month(self, date, type):
        if date:
            year, month, day = date.split('-')
            status = False if int(month) == 0 else True
        else:
            status = False
        return status

    def clean_day(self, date, type):
        if date:
            year, month, day = date.split('-')
            status = False if int(day) == 0 else True
        else:
            status = False
        return status


class AddRecordForm(ModelForm, DateSelectMixin):
    relationship_choices = ((choice.id, choice.label) for choice in ResidentRecordRelationship.objects.all())

    resident = forms.IntegerField(widget=forms.HiddenInput())
    relationship = forms.ChoiceField(choices=relationship_choices)
    category = forms.ChoiceField(choices=(('other', 'Other'), ('naa', 'NAA file or document')))

    def clean(self):
        cleaned_data = super(AddRecordForm, self).clean()
        if cleaned_data['category'] == 'naa':
            cleaned_data = self.get_naa_record(cleaned_data)
        return cleaned_data

    def get_naa_record(self, cleaned_data):
        barcode = cleaned_data['numeric_identifier']
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

        cleaned_data['is_part_of'] = series
        cleaned_data['record_type'] = item_type
        cleaned_data['identifier'] = item_details['control_symbol']
        cleaned_data['title'] = item_details['title']
        cleaned_data['date_string'] = dates['date_str']
        cleaned_data['start_date'] = dates['start_date']['date']
        cleaned_data['start_month_known'] = dates['start_date']['month']
        cleaned_data['start_day_known'] = dates['start_date']['day']
        cleaned_data['end_date'] = dates['end_date']['date']
        cleaned_data['end_month_known'] = dates['end_date']['month']
        cleaned_data['end_day_known'] = dates['end_date']['day']
        cleaned_data['access_status'] = item_details['access_status']
        cleaned_data['short_citation'] = citation
        cleaned_data['repository'] = repository
        cleaned_data['number_of_items'] = int(item_details['digitised_pages'])

        del self._errors['title']
        del self._errors['record_type']
        del self._errors['identifier']
        return cleaned_data

    class Meta:
        model = Record
        widgets = {
                    'title': forms.TextInput(attrs={'class': 'input-xxlarge'}),
                    'start_date': NewSelectDateWidget(attrs={'class': 'input-small'}, years=YEARS),
                    'start_date_month_known': forms.HiddenInput,
                    'start_date_day_known': forms.HiddenInput,
                    'end_date_month_known': forms.HiddenInput,
                    'end_date_day_known': forms.HiddenInput,
                    'end_date': NewSelectDateWidget(attrs={'class': 'input-small'}, years=YEARS),
                }


class UpdateRecordForm(ModelForm):
    relationship_choices = ((choice.id, choice.label) for choice in ResidentRecordRelationship.objects.all())

    barcode = forms.IntegerField()
    resident = forms.IntegerField(widget=forms.HiddenInput())
    relationship = forms.ChoiceField(choices=relationship_choices)


