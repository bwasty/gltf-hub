from rest_framework.routers import DefaultRouter

from gltf_models.views import GltfModelViewSet

router = DefaultRouter()
router.register(r'models', GltfModelViewSet)
urlpatterns = router.urls
