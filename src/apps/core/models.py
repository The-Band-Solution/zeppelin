from django.db import models
from django.utils.translation import gettext_lazy as _


class Historical(models.Model):
    """"""

    created_at = models.DateTimeField(auto_now_add=True)  # melhor que blank=True
    modified_at = models.DateTimeField(auto_now=True)



    class Meta:
        #db_table = 'historical'    
        abstract = True    

class Base(models.Model):
    """"""

    name = models.CharField(max_length=300, null=True, blank=True)
    description = models.CharField(max_length=300, null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)  # melhor que blank=True
    modified_at = models.DateTimeField(auto_now=True)


    class Meta:
        #db_table = 'base'
        abstract = True    

