from django.contrib.auth.models import User
from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticatedOrReadOnly

from gltf_models.models import GltfModel, GltfFile
from gltf_models.permissions import IsOwnerOrReadOnly
from gltf_models.serializers import GltfModelSerializer, GltfFileSerializer, UserSerializer


class GltfModelViewSet(viewsets.ModelViewSet):
    queryset = GltfModel.objects.all()
    serializer_class = GltfModelSerializer
    # TODO!: test for permissions
    permission_classes = [IsAuthenticatedOrReadOnly, IsOwnerOrReadOnly]

    def perform_create(self, serializer):
        serializer.save(uploader=self.request.user)

class GltfFileViewSet(viewsets.ModelViewSet):
    queryset = GltfFile.objects.all()
    serializer_class = GltfFileSerializer
    permission_classes = [IsAuthenticatedOrReadOnly, IsOwnerOrReadOnly]


# TODO!!! full upload view - options:
# https://stackoverflow.com/questions/39645410/how-to-upload-multiple-files-in-django-rest-framework
# https://stackoverflow.com/questions/52903232/how-to-upload-multiple-images-using-django-rest-framework
# https://stackoverflow.com/questions/52389956/uploading-multiple-files-using-django-rest-framework-without-using-forms
# https://stackoverflow.com/questions/37261710/uploading-multiples-image-with-django-rest-framework-in-a-single-post-array/37280575#37280575

class UserViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
