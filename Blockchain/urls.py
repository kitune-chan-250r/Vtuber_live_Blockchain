from rest_framework import routers
from .views import *

router = routers.DefaultRouter()
#router.register(r'api', VtuberViewSet)
#router.register(r'onlive', OnLiveViewSet)
router.register(r'transaction', TransactionViewSet)
