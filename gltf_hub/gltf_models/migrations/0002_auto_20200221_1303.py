# Generated by Django 3.0.3 on 2020-02-21 12:03

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import gltf_models.models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('gltf_models', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='gltfmodel',
            name='json',
        ),
        migrations.AddField(
            model_name='gltfmodel',
            name='preview_image',
            field=models.ImageField(null=True, upload_to=gltf_models.models._preview_image_upload_path),
        ),
        migrations.AddField(
            model_name='gltfmodel',
            name='public',
            field=models.BooleanField(default=True),
        ),
        migrations.AlterField(
            model_name='gltffile',
            name='file',
            field=models.FileField(upload_to=gltf_models.models._file_upload_path),
        ),
        migrations.AlterField(
            model_name='gltfmodel',
            name='uploader',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='gltfmodels', to=settings.AUTH_USER_MODEL),
        ),
    ]
