from django.core.files.storage import FileSystemStorage
from django.db import models
from django.conf import settings
from os.path import join
# Create your models here.
# fs = FileSystemStorage(location = join(settings.MEDIA_URL, 'photos'))

class ImageData(models.Model):
    photo = models.ImageField()
    base64_format = models.TextField()
    hash_format = models.CharField(max_length=128)

    def __str__(self):
        return f'{self.photo.name}'
