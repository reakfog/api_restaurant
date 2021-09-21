from rest_framework.serializers import ModelSerializer
from restaurant_project.apps.restaurant.models import Restaurant


class RestaurantSerializer(ModelSerializer):
    class Meta:
        model = Restaurant
        fields = ("user", "name", "description", "link")
        read_only_fields = ("user",)
