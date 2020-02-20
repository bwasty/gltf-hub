from rest_framework.routers import DefaultRouter

from gltf_models.views import GltfModelViewSet, GltfFileViewSet, UserViewSet

router = DefaultRouter()
router.register(r'models', GltfModelViewSet)
router.register(r'files', GltfFileViewSet)
router.register(r'users', UserViewSet)
urlpatterns = router.urls
