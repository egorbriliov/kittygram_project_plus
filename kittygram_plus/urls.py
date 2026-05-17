from rest_framework.routers import DefaultRouter

from django.urls import include, path

from cats.views import CatViewSet, OwnerViewSet, LightCatViewSet

router = DefaultRouter()
router.register('cats', CatViewSet, basename='cat')
router.register('owners', OwnerViewSet)
router.register(r'mycats', LightCatViewSet, basename='lightcats')

urlpatterns = [
    path('', include(router.urls)),
]
