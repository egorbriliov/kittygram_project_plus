"""Serializers for the Cat model."""
from rest_framework import serializers

from .models import Cat, Owner


class CatSerializer(serializers.ModelSerializer):
    """Serializer for the Cat model."""
    owner = serializers.HyperlinkedRelatedField(many=False,
                                                read_only=True,
                                                view_name='owner-detail')

    class Meta:
        """Meta class for the CatSerializer."""

        model = Cat
        fields = ('id', 'name', 'color', 'birth_year', 'owner')


class OwnerSerializer(serializers.ModelSerializer):
    """Serializer for the Owner model."""
    cats = serializers.HyperlinkedRelatedField(many=True,
                                               read_only=True,
                                               view_name='cat-detail')

    class Meta:
        """Meta class for the OwnerSerializer."""

        model = Owner
        fields = ('first_name', 'last_name', 'cats')
