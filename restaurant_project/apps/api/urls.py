from django.urls import include, path


urlpatterns = [
    path(r"restaurants/", include(("restaurant_project.apps.api.restaurants.urls", "restaurants"))),
]
