from rest_framework.routers import DefaultRouter
from django.urls import include, path
from cats.views import CatViewSet, OwnerViewSet, LightCatViewSet


class SafeDefaultRouter(DefaultRouter):
    include_format_suffixes = False


router = SafeDefaultRouter()
router.register('cats', CatViewSet, basename='cats')
router.register('owners', OwnerViewSet, basename='owners')
router.register(r'mycats', LightCatViewSet, basename='lightcats')

urlpatterns = [
    path('auth/', include('djoser.urls')),
    path('auth/', include('djoser.urls.jwt')),
    path('', include(router.urls)),
]
