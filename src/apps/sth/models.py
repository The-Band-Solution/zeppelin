from django.db import models
from django.utils.translation import gettext_lazy as _
from apps.core.models import Base


class Stage(Base):
    """"""

    class Meta:
        db_table = 'stage'

