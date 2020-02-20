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

    @property
    def owner(self):
        return self.uploader

def _upload_path(instance, filename):
    return f'models/{instance.model_id}/{filename}'

class GltfFile(models.Model):
    model = models.ForeignKey(GltfModel,
                              on_delete=models.CASCADE,
                              related_name='files')
    # TODO!!: auto-fill (save?) or remove??
    # the relative URI as specified in the JSON part of the model
    uri = models.CharField(max_length=128)
    # TODO!!: prevent duplication.... unique=True noe enough..overriding `save` seems possible
    file = models.FileField(upload_to=_upload_path)

    def __str__(self):
        return self.file.name

    @property
    def owner(self):
        return self.model.owner
