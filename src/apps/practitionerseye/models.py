from django.db import models
from django.utils.translation import gettext_lazy as _
from polymorphic.models import PolymorphicModel
from apps.core.models import Base


class Dimension(Base):
    """"""




    class Meta:
        db_table = 'dimension'

class Element(Base):
    """"""



    element_dimension = models.ForeignKey(Dimension, blank=True, null=True, on_delete=models.CASCADE, related_name="dimension_%(class)s")

    class Meta:
        db_table = 'element'

