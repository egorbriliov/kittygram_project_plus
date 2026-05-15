"""Serializers for the Cat model."""
from rest_framework import serializers

from .models import Cat, Owner


class CatSerializer(serializers.ModelSerializer):
    """Serializer for the Cat model."""

    class Meta:
        """Meta class for the CatSerializer."""

        model = Cat
        fields = ('id', 'name', 'color', 'birth_year')


class OwnerSerializer(serializers.ModelSerializer):
    """Serializer for the Owner model."""
    class Meta:
        """Meta class for the OwnerSerializer."""

        model = Owner
        fields = ('first_name', 'last_name')
