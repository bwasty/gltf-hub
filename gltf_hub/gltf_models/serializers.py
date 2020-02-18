from rest_framework import serializers

from gltf_models.models import GltfModel


class GltfModelSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = GltfModel
        fields = ['id', 'url', 'created_at', 'name', 'json']
