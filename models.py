from __future__ import unicode_literals

from django.db import models
from django.contrib.auth.models import User


class FileUploads(models.Model):
    filename = models.CharField(max_length=100, unique=True)
    uploaded_at = models.DateTimeField(auto_now_add=True)
    uploaded_by = models.ForeignKey(User)
    file = models.FileField(upload_to='uploads/%Y_%m_%d/')

    def __unicode__(self):
        return self.filename
