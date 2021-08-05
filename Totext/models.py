from django.db import models
from django.conf import settings
import uuid
import os
# Create your models here.
def get_file_path(instance, filename):
    ext = filename.split('.')[-1]
    filename = "%s.%s" % (uuid.uuid4(), ext)
    return os.path.join('image', filename)

class ImageUploadModel(models.Model):
    image = models.ImageField(upload_to=get_file_path, default=None)