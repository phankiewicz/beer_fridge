from rest_framework import (
    viewsets,
)

from .models import (
    Beer,
    BeerType,
    FridgeShelf,
)
from .serializers import (
    BeerSerializer,
    BeerTypeSerializer,
    FridgeShelfSerializer,
)


class BeerTypeViewSet(viewsets.ModelViewSet):
    serializer_class = BeerTypeSerializer
    queryset = BeerType.objects.all()


class BeerViewSet(viewsets.ModelViewSet):
    serializer_class = BeerSerializer
    queryset = Beer.objects.all()


class FridgeShelfViewSet(viewsets.ModelViewSet):
    serializer_class = FridgeShelfSerializer
    queryset = FridgeShelf.objects.all()
