from django.db import models

from base.models import BaseAbstractModel


class Tag(BaseAbstractModel):
    title = models.CharField(max_length=50)

