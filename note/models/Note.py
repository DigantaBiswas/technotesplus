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
    shared_with = models.ManyToManyField(User, related_name="shared_with",  blank=True)
    watched_by = models.ManyToManyField(User, related_name="watched_by",  blank=True)

    class Meta:
        app_label = 'note'

    def __str__(self):
        return self.title

    def update_watched_by_field(self, user):
        if user not in self.watched_by.all():
            self.watched_by.add(user)
            self.save()
