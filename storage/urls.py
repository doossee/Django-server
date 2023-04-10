from rest_framework.routers import DefaultRouter
from .views import ProductAPIViewSet, ClientAPIViewSet, AdventAPIViewSet, ConsumptionAPIViewSet, ProfitAPIViewSet


router = DefaultRouter()
router.register(r'products', ProductAPIViewSet)
router.register(r'clients', ClientAPIViewSet)
router.register(r'advents', AdventAPIViewSet)
router.register(r'consumptions', ConsumptionAPIViewSet)
router.register(r'profits', ProfitAPIViewSet)

urlpatterns = router.urls