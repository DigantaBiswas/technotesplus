from django.contrib.auth.models import User
from django.db import models

# Create your models here.
from base.models import BaseAbstractModel
from note.models.tag import Tag


class Note(BaseAbstractModel):
    title = models.CharField(max_length=255)
    body = models.TextField(blank=True, null=True)
    tag = models.ManyToManyField(Tag)
    created_by = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.title