from rest_framework import viewsets

from .models import Cat, Owner
from .serializers import CatSerializer, OwnerSerializer


class CatViewSet(viewsets.ModelViewSet):
    """API endpoint that allows cats to be viewed or edited."""

    queryset = Cat.objects.all()
    serializer_class = CatSerializer


class OwnerViewSet(viewsets.ModelViewSet):
    """API endpoint that allows owners to be viewed or edited."""

    queryset = Owner.objects.all()
    serializer_class = OwnerSerializer
