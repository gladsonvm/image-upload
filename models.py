from __future__ import unicode_literals

from django.db import models
from django.contrib.auth.models import User
from PIL import Image as Img
import StringIO
from django.core.files.uploadedfile import InMemoryUploadedFile


class FileUploads(models.Model):
    filename = models.CharField(max_length=100, unique=True)
    uploaded_at = models.DateTimeField(auto_now_add=True)
    uploaded_by = models.ForeignKey(User)
    image = models.ImageField(upload_to='uploads/%Y_%m_%d/')

    def save(self, *args, **kwargs):
        if self.image:
            img = Img.open(StringIO.StringIO(self.image.read()))
            if img.mode != 'RGB':
                img = img.convert('RGB')
            img.thumbnail((self.image.width / 1.5, self.image.height / 1.5), Img.ANTIALIAS)
            output = StringIO.StringIO()
            img.save(output, format='JPEG', quality=30)
            output.seek(0)
            self.image = InMemoryUploadedFile(output, 'ImageField', "%s.jpg" % self.image.name.split('.')[0],
                                              'image/jpeg', output.len, None)
        super(FileUploads, self).save(*args, **kwargs)

    def __unicode__(self):
        return self.filename
