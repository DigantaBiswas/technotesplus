from __future__ import absolute_import, unicode_literals

from celery import shared_task
from celery import app
from note.models.tag import Tag
from technotestplus.celery import app

@app.task
def task_number_one():
    tag = Tag(title="test_tag2")
    tag.save()
    print("hello world")