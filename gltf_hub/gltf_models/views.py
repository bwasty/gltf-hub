from rest_framework import viewsets

from gltf_models.models import GltfModel
from gltf_models.serializers import GltfModelSerializer


class GltfModelViewSet(viewsets.ModelViewSet):
    queryset = GltfModel.objects.all()
    serializer_class = GltfModelSerializer
    # TODO!!: owner or readonly...
    # permission_classes =
