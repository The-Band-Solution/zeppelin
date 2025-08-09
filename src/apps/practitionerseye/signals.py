from .models import Dimension, Element
from django.db.models.signals import (
    pre_init,   post_init,
    pre_save,   post_save,
    pre_delete, post_delete,
    m2m_changed
)
from django.dispatch import receiver
from django.contrib.auth.models import Group

## Signals from Dimension
@receiver(pre_init, sender=Dimension)
def pre_init_dimension(sender, *args, **kwargs):
    pass

@receiver(post_init, sender=Dimension)
def post_init_dimension(sender, instance, **kwargs):
    pass

@receiver(pre_save, sender=Dimension)
def pre_save_dimension(sender, instance, raw, using, update_fields, **kwargs):
    pass

@receiver(post_save, sender=Dimension)
def post_save_dimension(sender, instance, created, raw, using, update_fields, **kwargs):
    pass

@receiver(pre_delete, sender=Dimension)
def pre_delete_dimension(sender, instance, using, **kwargs):
    pass

@receiver(post_delete, sender=Dimension)
def post_delete_dimension(sender, instance, using, **kwargs):
    pass

@receiver(m2m_changed, sender=Dimension)
def m2m_changed_dimension(sender, instance, action, reverse, model, pk_set, using, **kwargs):
    pass


## Signals from Element
@receiver(pre_init, sender=Element)
def pre_init_element(sender, *args, **kwargs):
    pass

@receiver(post_init, sender=Element)
def post_init_element(sender, instance, **kwargs):
    pass

@receiver(pre_save, sender=Element)
def pre_save_element(sender, instance, raw, using, update_fields, **kwargs):
    pass

@receiver(post_save, sender=Element)
def post_save_element(sender, instance, created, raw, using, update_fields, **kwargs):
    pass

@receiver(pre_delete, sender=Element)
def pre_delete_element(sender, instance, using, **kwargs):
    pass

@receiver(post_delete, sender=Element)
def post_delete_element(sender, instance, using, **kwargs):
    pass

@receiver(m2m_changed, sender=Element)
def m2m_changed_element(sender, instance, action, reverse, model, pk_set, using, **kwargs):
    pass

