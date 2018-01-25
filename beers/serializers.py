from rest_framework import (
    serializers,
)

from .models import (
    Beer,
    BeerType,
    FridgeShelf,
)


class BeerTypeSerializer(serializers.ModelSerializer):

    class Meta:
        model = BeerType
        fields = (
            'id',
            'name',
            'serving_temperature',
        )


class BeerSerializer(serializers.ModelSerializer):

    type_info = BeerTypeSerializer(
        read_only=True,
        source="type",
    )

    class Meta:
        model = Beer
        fields = (
            'id',
            'name',
            'type',
            'type_info',
            'image',
        )


class FridgeShelfSerializer(serializers.ModelSerializer):

    class Meta:
        model = FridgeShelf
        fields = (
            'id',
            'beer',
            'current_temperature',
        )
