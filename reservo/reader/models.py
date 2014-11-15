# -*- coding: utf-8 -*-
from urlparse import urlparse

from django.db import models

class Story(models.Model):
    id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=200)
    url = models.URLField()
    score = models.IntegerField()
    submitter = models.CharField(max_length=100)
    timestamp = models.DateTimeField()
    updated_at = models.DateTimeField(auto_now_add=True)
    hn_id = models.IntegerField()

    def __unicode__(self):
        return self.title
