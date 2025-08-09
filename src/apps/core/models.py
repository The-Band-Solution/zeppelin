from django.db import models
from django.utils.translation import gettext_lazy as _
from polymorphic.models import PolymorphicModel


class Historical(PolymorphicModel,models.Model):
    """"""

    created_at = models.DateTimeField(auto_now_add=True)  # melhor que blank=True
    modified_at = models.DateTimeField(auto_now=True)



    class Meta:
        db_table = 'historical'    
        #abstract = True    

class Base(PolymorphicModel, models.Model):
    """"""

    nome = models.CharField(max_length=300, null=True, blank=True)
    descricao = models.CharField(max_length=300, null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)  # melhor que blank=True
    modified_at = models.DateTimeField(auto_now=True)


    class Meta:
        db_table = 'base'
        #abstract = True    

