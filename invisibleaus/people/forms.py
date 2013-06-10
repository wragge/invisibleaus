from django import forms
from django.forms import ModelForm
from django.forms.extras.widgets import SelectDateWidget
from django.forms.models import inlineformset_factory
from calendar import monthrange

from invisibleaus.people.models import *
from invisibleaus.generic.forms import AddPersonForm


YEARS = [year for year in range(1800, 1960)]


class NewSelectDateWidget(SelectDateWidget):
    none_value = (0, 'unknown')


class ResidentNamePartInline(ModelForm):
    model = ResidentNamePart


class AddResidentNameForm(ModelForm):
    resident = forms.ModelChoiceField(queryset=Resident.objects.all(), widget=forms.HiddenInput())

    class Meta:
        model = ResidentAltName
        widgets = {
                    'note': forms.Textarea(attrs={'rows': '4'})

                }


ResidentNamePartInlineFormset = inlineformset_factory(
    ResidentAltName,
    ResidentNamePart,
    #form=ResidentNamePartInline,
    extra=1,
    can_delete=True,
    can_order=False
)


class AddResidentForm(AddPersonForm):

    class Meta:
        model = Resident
        exclude = ('related_residents', 'related_record_aggregations')
        widgets = {
                    'display_name': forms.TextInput(attrs={'class': 'input-xxlarge'}),
                    'birth_earliest_date': NewSelectDateWidget(attrs={'class': 'input-small'}, years=YEARS),
                    'birth_earliest_date_month_known': forms.HiddenInput,
                    'birth_earliest_date_day_known': forms.HiddenInput,
                    'birth_latest_date_month_known': forms.HiddenInput,
                    'birth_latest_date_day_known': forms.HiddenInput,
                    'birth_latest_date': NewSelectDateWidget(attrs={'class': 'input-small'}, years=YEARS),
                    'death_earliest_date': NewSelectDateWidget(attrs={'class': 'input-small'}, years=YEARS),
                    'death_earliest_date_month_known': forms.HiddenInput,
                    'death_earliest_date_day_known': forms.HiddenInput,
                    'death_latest_date_month_known': forms.HiddenInput,
                    'death_latest_date_day_known': forms.HiddenInput,
                    'death_latest_date': NewSelectDateWidget(attrs={'class': 'input-small'}, years=YEARS),
                }
