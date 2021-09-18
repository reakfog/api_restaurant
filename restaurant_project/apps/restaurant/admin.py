from django.contrib.admin import ModelAdmin, register
from restaurant_project.apps.restaurant.models import Restaurant


@register(Restaurant)
class RestaurantAdmin(ModelAdmin):
    pass