from django.contrib.postgres.fields import JSONField
from django.db import models

class GltfModel(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    name = models.CharField(max_length=64)
    json = JSONField()  # jsonb
    uploader = models.ForeignKey('auth.User',
                                 related_name='gltfmodels',
                                 on_delete=models.SET_NULL, # TODO!: cascade?
                                 null=True)  # TODO!: not null?

    def __str__(self):
        return self.name

class GltfFile(models.Model):
    model = models.ForeignKey(GltfModel,
                              on_delete=models.CASCADE,
                              related_name='files')
    # the relative URI as specified in the JSON part of the model
    uri = models.CharField(max_length=128)
    # TODO!!: upload_to callable, containing model id?
    file = models.FileField(upload_to='uploads/')

    def __str__(self):
        return self.file.name
