from api.views import DummyViewSet
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register(r'dummy', DummyViewSet, basename='dummy')
urlpatterns = router.urls
