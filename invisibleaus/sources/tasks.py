from rstools import client
from invisibleaus.sources.models import *
from invisibleaus.people.models import Repository


def harvest_series(series_id):
    rs = client.RSSeriesClient()
    details = rs.get_summary(series_id)
    record_type = RecordType.objects.get(label='series')
    repository = Repository.objects.get(display_name='National Archives of Australia')
    series = Series.objects.get_or_create(
                                identifier=details['identifier'],
                                record_type=record_type,
                                repository=repository,
                                defaults={
                                    'title': details['title'],

                                }
                            )



