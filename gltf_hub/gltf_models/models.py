from django.contrib.postgres.fields import JSONField
from django.db import models

class GltfModel(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    name = models.CharField(max_length=64)
    json = JSONField()  # jsonb

# class GltfFile(models.Model):
#     model = models.ForeignKey(GltfModel, on_delete=models.CASCADE)
#     # the relative URI as specified in the JSON part of the model
#     uri = models.CharField(max_length=128)
#     # TODO!!: MEDIA_ROOT, MEDIA_URL, ... see https://docs.djangoproject.com/en/3.0/ref/models/fields/#django.db.models.FileField.storage
#     file = models.FileField(upload_to='uploads/')
