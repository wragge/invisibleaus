from django.db import models

# Create your models here.


class NSWBDMRegister(models.Model):
    surname = models.CharField(max_length=100, blank=True, null=True)
    given_names = models.CharField(max_length=100, blank=True, null=True)
    event_type = models.CharField(max_length=1, blank=True, null=True)
    index_year = models.IntegerField(blank=True, null=True)
    father_spouse_surname = models.CharField(max_length=100, blank=True, null=True)
    mother_spouses_names = models.CharField(max_length=100, blank=True, null=True)
    registration_place = models.CharField(max_length=100, blank=True, null=True)
    volume_reference = models.CharField(max_length=20, blank=True, null=True)
    registration_year = models.IntegerField(blank=True, null=True)
    registration_number = models.CharField(max_length=20, blank=True, null=True)

    def get_identifier(self):
        if self.registration_number:
            identifier = '{}/{}'.format(self
                                    .registration_year,
                                    self.registration_number
                                    )
        elif self.volume_reference:
            identifier = self.volume_reference
        else:
            identifier = 'No id'
        return identifier

    def highlight_duplicates(self):
        results = (
                    NSWBDMRegister.objects
                    .filter(registration_year=self.registration_year)
                    .filter(registration_number=self.registration_number)
                    .count()
                )
        if results > 1:
            identifier = '<span style="color: red; font-weight: bold;">{}</span>'.format(self.get_identifier())
        else:
            identifier = self.get_identifier()
        return identifier

    highlight_duplicates.allow_tags = True
