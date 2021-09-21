from random import choice

from rest_framework.decorators import action
from rest_framework.exceptions import NotFound
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from rest_framework.response import Response
from rest_framework.status import HTTP_200_OK
from rest_framework.viewsets import ModelViewSet
from restaurant_project.apps.api.restaurants.serializers import RestaurantSerializer
from restaurant_project.apps.restaurant.models import Restaurant
from restaurant_project.apps.utils.permissions import IsAuthorOrReadOnly


class RestaurantViewSet(ModelViewSet):
    queryset = Restaurant.objects.all()
    serializer_class = RestaurantSerializer
    permission_classes = [IsAuthenticatedOrReadOnly, IsAuthorOrReadOnly]
    lookup_field = "name"

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

    @action(["get"], detail=False, pagination_class=None)
    def random(self, request, *args, **kwargs):
        restaurants = self.get_queryset()
        if not restaurants:
            raise NotFound()
        random_restaurant = choice(restaurants)
        serializer = self.get_serializer(random_restaurant)

        return Response(serializer.data, status=HTTP_200_OK)
