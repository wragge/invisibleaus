# Create your views here.
from django.views.generic.edit import CreateView, UpdateView, DeleteView, FormView
from invisibleaus.linkeddata.views import LinkedDataView, LinkedDataListView
from invisibleaus.sources.models import *
from invisibleaus.sources.forms import AddRecordForm
from invisibleaus.people.models import *
from django.http import HttpResponseRedirect

class AggregationView(LinkedDataView):
    model = Record
    path = '/records/%s'
    template_name = 'sources/record_aggregation'

    def make_graph(self, entity):
        namespaces = {}
        graph = Graph()
        schemas = RDFSchema.objects.all()
        for schema in schemas:
            namespace = Namespace(schema.uri)
            graph.bind(schema.prefix, namespace)
            namespaces[schema.prefix] = namespace
        host_ns = Namespace('http://%s' % (Site.objects.get_current().domain))
        this_person = URIRef(host_ns[entity.get_absolute_url()])
        graph.add((this_person, namespaces['rdf']['type'], namespaces['foaf']['Person']))
        graph.add((this_person, namespaces['rdfs']['label'], Literal(str(entity))))
        graph.add((this_person, namespaces['foaf']['name'], Literal(str(entity))))
        return graph


class AggregationListView(LinkedDataListView):
    model = Record
    path = '/records/results'
    template_name = 'sources/record_aggregations'

    def make_graph(self, entities):
        namespaces = {}
        graph = Graph()
        schemas = RDFSchema.objects.all()
        for schema in schemas:
            namespace = Namespace(schema.uri)
            graph.bind(schema.prefix, namespace)
            namespaces[schema.prefix] = namespace
        host_ns = Namespace('http://%s' % (Site.objects.get_current().domain))
        for entity in entities:
            this_person = URIRef(host_ns[entity.get_absolute_url()])
            graph.add((this_person, namespaces['rdf']['type'], namespaces['foaf']['Person']))
            graph.add((this_person, namespaces['rdfs']['label'], Literal(str(entity))))
        return graph


class RecordCreateView(CreateView):
    form_class = AddRecordForm
    template_name = 'sources/add_record.html'
    model = Record

    def get_initial(self):
        initial = super(RecordCreateView, self).get_initial()
        entity_id = self.kwargs.get('entity_id', None)
        entity_type = self.kwargs.get('entity_type', None)
        initial[entity_type] = entity_id
        return initial

    def get_context_data(self, **kwargs):
        context = super(RecordCreateView, self).get_context_data(**kwargs)
        if self.request.POST:
            #resident_id = self.cleaned_data['resident']
            pass
        else:
            resident_id = self.kwargs.get('entity_id', None)
            resident = Resident.objects.get(id=resident_id)
            context['resident_name'] = resident.display_name
        context.update(kwargs)
        return context

    def form_valid(self, form):
        #self.get_naa_record(form)
        record = form.save(commit=False)
        record.save()
        resident = Resident.objects.get(id=form.cleaned_data['resident'])
        if resident:
            relationship = ResidentRecordRelationship.objects.get(id=form.cleaned_data['relationship'])
            ResidentRelatedRecord.objects.create(
                    resident=resident,
                    record=record,
                    relationship=relationship
                )
        return HttpResponseRedirect(reverse('record_view', args=[record.id]))


class RecordUpdateView(UpdateView):
    form_class = AddRecordForm
    template_name = 'sources/update_record.html'
    model = Record

