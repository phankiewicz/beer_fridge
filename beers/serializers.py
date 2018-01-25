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

    beer_info = BeerSerializer(
        read_only=True,
        source="beer",
    )

    class Meta:
        model = FridgeShelf
        fields = (
            'id',
            'beer',
            'beer_info',
            'current_temperature',
        )
