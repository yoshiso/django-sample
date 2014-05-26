# -*- coding: utf-8 -*-
from django.db import models
from django.utils import timezone
import datetime

# Create your models here.

class Poll(models.Model):
    """Poll Model Object"""

    question = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published')


    def was_published_recently(self):
        return timezone.now() > self.pub_date >= timezone.now() - datetime.timedelta(days=1)
    was_published_recently.admin_order_field='pub_date'
    was_published_recently.boolean=True
    was_published_recently.short_description = 'Published recently'

    def __unicode__(self):
        return self.question


class Choice(models.Model):
    """docstring for Choice"""

    poll = models.ForeignKey(Poll)
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)

    def __unicode__(self):
        return self.choice_text

