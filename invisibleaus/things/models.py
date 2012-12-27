from django.db import models
from invisibleaus.linkeddata.models import RDFRelationship, RDFType
from invisibleaus.generic.models import Event, Period, Person, Thing, StandardMetadata

# Create your models here.


class Ship(Thing):
    ''' A ship. '''
