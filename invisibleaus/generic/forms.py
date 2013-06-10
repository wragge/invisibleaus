from django import forms
from django.forms import ModelForm
from django.forms.extras.widgets import SelectDateWidget
from calendar import monthrange


class NewSelectDateWidget(SelectDateWidget):
    none_value = (0, 'unknown')


class AddPersonForm(ModelForm):
    years = [year for year in range(1850, 1950)]

    birth_earliest_date = forms.CharField(widget=NewSelectDateWidget(attrs={'class': 'input-small'}, years=years), required=False)
    birth_latest_date = forms.CharField(widget=NewSelectDateWidget(attrs={'class': 'input-small'}, years=years), required=False)
    birth_earliest_month_known = forms.BooleanField(widget=forms.HiddenInput, required=False)
    birth_earliest_day_known = forms.BooleanField(widget=forms.HiddenInput, required=False)
    birth_latest_month_known = forms.BooleanField(widget=forms.HiddenInput, required=False)
    birth_latest_day_known = forms.BooleanField(widget=forms.HiddenInput, required=False)
    death_earliest_date = forms.CharField(widget=NewSelectDateWidget(attrs={'class': 'input-small'}, years=years), required=False)
    death_latest_date = forms.CharField(widget=NewSelectDateWidget(attrs={'class': 'input-small'}, years=years), required=False)
    death_earliest_month_known = forms.BooleanField(widget=forms.HiddenInput, required=False)
    death_earliest_day_known = forms.BooleanField(widget=forms.HiddenInput, required=False)
    death_latest_month_known = forms.BooleanField(widget=forms.HiddenInput, required=False)
    death_latest_day_known = forms.BooleanField(widget=forms.HiddenInput, required=False)

    def clean_birth_earliest_date(self):
        return self.clean_date(self.cleaned_data['birth_earliest_date'], 'start')

    def clean_death_earliest_date(self):
        return self.clean_date(self.cleaned_data['death_earliest_date'], 'start')

    def clean_birth_latest_date(self):
        return self.clean_date(self.cleaned_data['birth_latest_date'], 'end')

    def clean_death_latest_date(self):
        return self.clean_date(self.cleaned_data['death_latest_date'], 'end')

    def clean_birth_earliest_month_known(self):
        return self.clean_month(self.cleaned_data['birth_earliest_date'], 'start')

    def clean_death_earliest_month_known(self):
        return self.clean_month(self.cleaned_data['death_earliest_date'], 'start')

    def clean_birth_earliest_day_known(self):
        return self.clean_day(self.cleaned_data['birth_earliest_date'], 'start')

    def clean_death_earliest_day_known(self):
        return self.clean_day(self.cleaned_data['death_earliest_date'], 'start')

    def clean_birth_latest_month_known(self):
        return self.clean_month(self.cleaned_data['birth_latest_date'], 'end')

    def clean_death_latest_month_known(self):
        return self.clean_month(self.cleaned_data['death_latest_date'], 'end')

    def clean_birth_latest_day_known(self):
        return self.clean_day(self.cleaned_data['birth_latest_date'], 'end')

    def clean_death_latest_day_known(self):
        return self.clean_day(self.cleaned_data['death_latest_date'], 'end')

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
            month = False if int(month) == 0 else True
        else:
            month = False
        return month

    def clean_day(self, date, type):
        if date:
            year, month, day = date.split('-')
            day = False if int(day) == 0 else True
        else:
            day = False
        return day
