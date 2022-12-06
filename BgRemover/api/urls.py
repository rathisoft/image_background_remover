from BgRemover.api.views import ImageViewSet
from rest_framework import routers
from django.urls import path, include

router = routers.DefaultRouter()
router.register(r'BgRemover', ImageViewSet)

urlpatterns = [
    path('', include(router.urls))
]