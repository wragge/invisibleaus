from django.conf.urls import patterns, include, url
from django.conf import settings

from django.contrib import admin

from invisibleaus.people.views import *
from invisibleaus.sources.views import *

admin.autodiscover()

urlpatterns = patterns('',
    url(r'^admin/', include(admin.site.urls)),
)

urlpatterns += patterns('invisibleaus.people.views',
    url(r'^residents/$', ResidentListView.as_view(), name="resident_list"),
    url(r'^residents/results\.(?P<format>(html|rdf|json|ttl))/$', ResidentListView.as_view()),
    url(r'^residents/(?P<id>\d+)\.(?P<format>(html|rdf|json|ttl))/$', ResidentView.as_view()),
    url(r'^residents/(?P<id>\d+)/$', ResidentView.as_view(), name='resident-view'),
    #url(r'^residents/add/$', ResidentCreate.as_view(), name='resident-add'),
    #url(r'^residents/update/(?P<pk>\d+)/$', ResidentUpdate.as_view(), name='resident-update'),
    #url(r'^residents/delete/(?P<id>\d+)/$', ResidentDelete.as_view(), name='resident_delete'),
    #url(r'^residents/(?P<resident_id>\d+)/name/create/$', ResidentNameCreate.as_view(), name='resident-name-add'),
    #url(r'^residents/name/(?P<pk>\d+)/update/$', ResidentNameUpdate.as_view(), name='resident-name-update'),
)

urlpatterns += patterns('invisibleaus.sources.views',
    url(r'^records/$', AggregationListView.as_view(), name="resident_list"),
    url(r'^records/results\.(?P<format>(html|rdf|json|ttl))/$', AggregationListView.as_view()),
    url(r'^records/(?P<id>\d+)\.(?P<format>(html|rdf|json|ttl))/$', AggregationView.as_view()),
    url(r'^records/(?P<id>\d+)/$', AggregationView.as_view(), name='record-view'),
    #url(r'^records/add/$', RecordCreateView.as_view(), name='record-add'),
    #url(r'^records/(?P<id>\d+)/$', RecordUpdateView.as_view(), name='record-update'),
    #url(r'^records/(?P<id>\d+)/delete/$', RecordDelete.as_view(), name='record-delete'),
    #url(r'^records/add/(?P<entity_type>resident)/(?P<entity_id>\d+)/$', RecordCreateView.as_view(), name='record-add-entity'),
)

urlpatterns += patterns('',
    url(r'^accounts/', include('registration.backends.default.urls')),
)

if settings.DEBUG:
    urlpatterns = patterns('',
    url(r'^media/(?P<path>.*)$', 'django.views.static.serve',
        {'document_root': settings.MEDIA_ROOT, 'show_indexes': True}),
    url(r'', include('django.contrib.staticfiles.urls')),
) + urlpatterns
