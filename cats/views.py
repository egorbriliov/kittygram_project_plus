from rest_framework import viewsets, serializers
# from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework import mixins
from django.shortcuts import get_object_or_404

from .models import Cat, Owner, CHOICES
from .serializers import CatSerializer, OwnerSerializer


class UpdateDeleteViewSet(mixins.UpdateModelMixin,
                          mixins.DestroyModelMixin,
                          viewsets.GenericViewSet):
    """ViewSet for updating and deleting objects."""
    pass


class CreateRetrieveViewSet(mixins.CreateModelMixin,
                            mixins.RetrieveModelMixin,
                            viewsets.GenericViewSet):
    """ViewSet for creating and retrieving objects."""
    pass


class LightCatViewSet(CreateRetrieveViewSet):
    """API endpoint that allows cats to be viewed or edited with limited fields."""

    queryset = Cat.objects.all()
    serializer_class = CatSerializer


class CatListSerializer(serializers.ModelSerializer):
    """Serializer for listing cats with limited fields."""
    color = serializers.ChoiceField(choices=CHOICES)

    class Meta:
        model = Cat
        fields = ['id', 'name', 'color']


# class CatViewSet(viewsets.ModelViewSet):
#     """API endpoint that allows cats to be viewed or edited."""

#     queryset = Cat.objects.all()
#     serializer_class = CatSerializer

#     def get_serializer_class(self):
#         """Return the appropriate serializer class based on the action."""
#         if self.action == 'list':
#             return CatListSerializer
#         return CatSerializer

#     @action(detail=False, url_path='recent-white-cats')
#     def recent_white_cats(self, request):
#         """Custom action to retrieve recent white cats."""
#         recent_white_cats = Cat.objects.filter(color='White')[:5]
#         serializer = self.get_serializer(recent_white_cats, many=True)
#         return Response(serializer.data)

class CatViewSet(viewsets.ViewSet):
    """API endpoint that allows cats to be viewed or edited."""

    def list(self, request):
        queryset = Cat.objects.all()
        serializer = CatListSerializer(queryset, many=True)
        return Response(serializer.data)

    def retrieve(self, request, pk=None):
        queryset = Cat.objects.all()
        cat = get_object_or_404(queryset, pk=pk)
        serializer = CatSerializer(cat)
        return Response(serializer.data)


class OwnerViewSet(viewsets.ModelViewSet):
    """API endpoint that allows owners to be viewed or edited."""

    queryset = Owner.objects.all()
    serializer_class = OwnerSerializer
