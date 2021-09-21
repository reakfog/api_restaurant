from django.urls import include, path
from rest_framework.routers import DefaultRouter
from restaurant_project.apps.api.restaurants.views import RestaurantViewSet

router = DefaultRouter()
router.register("", RestaurantViewSet)

urlpatterns = [
    path("", include(router.urls)),
]
