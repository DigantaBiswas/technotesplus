from django.db import models

from base.models import BaseAbstractModel


class Tag(BaseAbstractModel):
    name = models.CharField(max_length=50)

