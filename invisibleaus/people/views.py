from django.shortcuts import render_to_response, render, get_object_or_404
from django.views.generic.edit import CreateView, UpdateView, DeleteView, FormView
from django.core.urlresolvers import reverse_lazy
from django.http import HttpResponseRedirect
from django.shortcuts import redirect

from invisibleaus.linkeddata.views import LinkedDataView, LinkedDataListView
from invisibleaus.people.forms import *
from invisibleaus.sources.models import *

from rstools.retrieve import RSSeriesClient, RSItemClient


class ResidentView(LinkedDataView):
    model = Resident
    path = '/residents/%s'
    template_name = 'people/resident'

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


class ResidentListView(LinkedDataListView):
    model = Resident
    path = '/residents/results'
    template_name = 'people/residents'

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


class PapertrailsListView(LinkedDataListView):
    queryset = Resident.objects.filter(papertrails=True)

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


class ResidentCreate(CreateView):
    form_class = AddResidentForm
    model = Resident
    template_name = 'people/add_resident.html'

    def get_success_url(self):
        return reverse_lazy('resident-update', kwargs={'pk': self.object.id})

    def form_valid(self, form):
        self.object = form.save(commit=False)
        self.object.save()
        return redirect(self.get_success_url())


class DummyCreate():

    def get_success_url(self):
        return reverse('resident-view')

    def form_valid(self, form):
        context = self.get_context_data()
        alt_names = context['alt_names']
        alt_name_parts = context['alt_name_parts']
        if alt_names.is_valid() and form.is_valid():
            self.object = form.save(commit=False)
            self.object.save()
            return redirect(self.success_url)
        else:
            return self.render_to_response(self.get_context_data(form=form))

    def form_invalid(self, form):
        return self.render_to_response(self.get_context_data(form=form))

    def get_context_data(self, **kwargs):
        context = super(ResidentCreate, self).get_context_data(**kwargs)
        if self.request.POST:
            context['form'] = AddResidentForm(self.request.POST)
            context['alt_names'] = ResidentNameInlineFormset(self.request.POST)
            context['alt_name_parts'] = ResidentNamePartInlineFormset()
        else:
            context['form'] = AddResidentForm()
            context['alt_names'] = ResidentNameInlineFormset()
            context['alt_name_parts'] = ResidentNamePartInlineFormset()
        return context


class ResidentUpdate(UpdateView):
    form_class = AddResidentForm
    model = Resident
    template_name = 'people/add_resident.html'

    def get_success_url(self):
        return reverse_lazy('resident-update', kwargs={'pk': self.object.id})

    def form_valid(self, form):
        self.object = form.save(commit=False)
        self.object.save()
        return redirect(self.get_success_url())

    def prepare_date(self, name):
        date = getattr(self.object, '{}_date'.format(name))
        if date:
            year = date.year
            month = date.month
            day = date.day
            if getattr(self.object, '{}_month_known'.format(name)) is False:
                month = 0
            if getattr(self.object, '{}_day_known'.format(name)) is False:
                day = 0
            date = '{}-{}-{}'.format(year, month, day)
            print date
        return date

    def get_initial(self):
        initial = {}
        initial['birth_earliest_date'] = self.prepare_date('birth_earliest')
        initial['birth_latest_date'] = self.prepare_date('birth_latest')
        initial['death_earliest_date'] = self.prepare_date('death_earliest')
        initial['death_latest_date'] = self.prepare_date('death_latest')
        return initial


class ResidentDelete(DeleteView):
    form_class = AddResidentForm
    model = Resident
    template_name = 'people/add_resident.html'


class ResidentNameCreate(CreateView):
    form_class = AddResidentNameForm
    model = ResidentAltName
    template_name = 'people/add_resident_name.html'

    def get_success_url(self):
        return reverse_lazy('resident-update', kwargs={'pk': self.object.resident.id})

    def get_initial(self):
        resident_id = self.kwargs.get('resident_id', None)
        initial = {'resident': resident_id}
        return initial

    def form_valid(self, form):
        context = self.get_context_data()
        namepart_formset = context['namepart_formset']
        if namepart_formset.is_valid() and form.is_valid():
            self.object = form.save()
            namepart_formset.instance = self.object
            namepart_formset.save()
            return redirect(self.get_success_url())
        else:
            return self.render_to_response(self.get_context_data(form=form))

    def form_invalid(self, form):
        return self.render_to_response(self.get_context_data(form=form))

    def get_context_data(self, **kwargs):
        context = super(ResidentNameCreate, self).get_context_data(**kwargs)
        if self.request.POST:
            #context['form'] = AddResidentNameForm(self.request.POST)
            context['namepart_formset'] = ResidentNamePartInlineFormset(self.request.POST)
        else:
            #context['form'] = AddResidentNameForm()
            context['namepart_formset'] = ResidentNamePartInlineFormset()
        resident_id = self.kwargs.get('resident_id', None)
        resident = Resident.objects.get(id=resident_id)
        context['resident'] = resident
        context.update(kwargs)
        return context


class ResidentNameUpdate(UpdateView):
    form_class = AddResidentNameForm
    model = ResidentAltName
    template_name = 'people/add_resident_name.html'

    def get_success_url(self):
        return reverse_lazy('resident_update', kwargs={'pk': self.object.resident.id})

    def form_valid(self, form):
        context = self.get_context_data()
        namepart_formset = context['namepart_formset']
        if namepart_formset.is_valid() and form.is_valid():
            self.object = form.save()
            namepart_formset.instance = self.object
            namepart_formset.save()
            return redirect(self.get_success_url())
        else:
            return self.render_to_response(self.get_context_data(form=form))

    def form_invalid(self, form):
        return self.render_to_response(self.get_context_data(form=form))

    def get_context_data(self, **kwargs):
        context = super(ResidentNameUpdate, self).get_context_data(**kwargs)
        if self.request.POST:
            #context['form'] = AddResidentNameForm(self.request.POST)
            context['namepart_formset'] = ResidentNamePartInlineFormset(self.request.POST, instance=self.object)
        else:
            #context['form'] = AddResidentNameForm()
            context['namepart_formset'] = ResidentNamePartInlineFormset(instance=self.object)
        context.update(kwargs)
        return context
