from django.db import models
from django.utils.translation import gettext_lazy as _
from polymorphic.models import PolymorphicModel
from apps.core.models import Base


class OrganizationCategory(Base):
    """"""




    class Meta:
        db_table = 'organizationcategory'

class Size(Base):
    """"""




    class Meta:
        db_table = 'size'

class OrganizationType(Base):
    """"""



    category = models.ForeignKey(OrganizationCategory, blank=True, null=True, on_delete=models.CASCADE, related_name="category_%(class)s")

    class Meta:
        db_table = 'organizationtype'

class Region(Base):
    """"""




    class Meta:
        db_table = 'region'

class State(Base):
    """"""

    latitude = models.DecimalField(max_digits=14, decimal_places=2, null=True, blank=True)
    longitude = models.DecimalField(max_digits=14, decimal_places=2, null=True, blank=True)


    region = models.ForeignKey(Region, blank=True, null=True, on_delete=models.CASCADE, related_name="region_%(class)s")

    class Meta:
        db_table = 'state'

class Organization(Base):
    """"""

    age = models.IntegerField(null=True, blank=True)


    type = models.ForeignKey(OrganizationType, blank=True, null=True, on_delete=models.CASCADE, related_name="type_%(class)s")
    size = models.ForeignKey(Size, blank=True, null=True, on_delete=models.CASCADE, related_name="size_%(class)s")
    location = models.ForeignKey(State, blank=True, null=True, on_delete=models.CASCADE, related_name="location_%(class)s")

    class Meta:
        db_table = 'organization'

