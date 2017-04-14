from __future__ import unicode_literals

from django.db import models


class Event(models.Model):
    date = models.DateField()
    summary = models.CharField(max_length=100)
    link = models.URLField()
    visible = models.BooleanField()

    def __str__(self):
        return str(self.date) + ' - ' + self.summary
