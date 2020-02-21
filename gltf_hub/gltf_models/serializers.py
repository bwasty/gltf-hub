from django.contrib.auth.models import User
from rest_framework import serializers

from gltf_models.models import GltfModel, GltfFile


class GltfModelSerializer(serializers.HyperlinkedModelSerializer):
    uploader = serializers.ReadOnlyField(source='uploader.username')

    class Meta:
        model = GltfModel
        fields = ['id', 'url', 'created_at', 'name', 'files', 'preview_image', 'uploader', 'public']

class GltfFileSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = GltfFile
        # TODO!!: better file serialization - current: http://localhost:8000/media/uploads/Box0.bin
        fields = ['id', 'url', 'model', 'uri', 'file']

class UserSerializer(serializers.HyperlinkedModelSerializer):
    gltfmodels = serializers.HyperlinkedRelatedField(many=True, view_name='gltfmodel-detail', read_only=True)

    class Meta:
        model = User
        fields = ['url', 'id', 'username', 'gltfmodels']
