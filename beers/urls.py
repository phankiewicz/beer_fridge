from django.conf.urls import (
    include,
    url,
)

from rest_framework import routers

from .viewsets import (
    BeerViewSet,
    BeerTypeViewSet,
    FridgeShelfViewSet,
)

router_v1 = routers.DefaultRouter()

router_v1.register(
    r'beers',
    BeerViewSet,
    base_name='beers',
)
router_v1.register(
    r'beer_types',
    BeerTypeViewSet,
    base_name='beer_types',
)
router_v1.register(
    r'fridge_shelves',
    FridgeShelfViewSet,
    base_name='fridge_shelves',
)

urlpatterns = (
    url(
        r'^v1/',
        include(
            router_v1.urls,
            namespace='v1_beers',
        ),
    ),
)
