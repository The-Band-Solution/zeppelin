from django.db import models
from django.utils.translation import gettext_lazy as _
from polymorphic.models import PolymorphicModel


class Historical(PolymorphicModel, models.Model):
    """"""

    create_at = models.DateTimeField(blank=True)
    modified_at = models.DateTimeField(blank=True)



    class Meta:
        db_table = 'historical'

class Base(Historical):
    """"""

    nome = models.CharField(max_length=300, null=True, blank=True)
    descricao = models.CharField(max_length=300, null=True, blank=True)



    class Meta:
        db_table = 'base'

