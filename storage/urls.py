from rest_framework.routers import DefaultRouter
from .views import ProductAPIViewSet, ClientAPIViewSet, AdventListAPIViewSet, ConsumptionListAPIViewSet, ProfitAPIViewSet


router = DefaultRouter()
router.register(r'products', ProductAPIViewSet)
router.register(r'clients', ClientAPIViewSet)
router.register(r'advents', AdventListAPIViewSet)
router.register(r'consumptions', ConsumptionListAPIViewSet)
router.register(r'profits', ProfitAPIViewSet)

urlpatterns = router.urls