from __future__ import unicode_literals
from django.db import models
from django.utils import timezone

class Feedback(models.Model):
    name = models.CharField(max_length=200)
    phone = models.CharField(max_length=20)
    text = models.TextField()
    created_date = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.name + ' ' + self.phone


