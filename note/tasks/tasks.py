from __future__ import absolute_import, unicode_literals

from celery import shared_task
from celery import app
from django.contrib.auth.models import User

from note.models.Note import Note
from note.models.tag import Tag
from technotestplus.celery import app


def get_unwatch_shared_posts():
    all_notes = Note.objects.filter(all_watched=False)
    for note in all_notes:
        users = User.objects.filter(id__in=list(note.shared_with.all().values_list("id", flat=True))).exclude(
            id__in=list(note.watched_by.all().values_list("id", flat=True)))
        for user in users:
            email = user.email
            # if email:




@app.task
def task_number_one():
    tag = Tag(title="test_tag2")
    tag.save()
    print("hello world")
