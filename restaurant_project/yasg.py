from django.urls import path, re_path
from drf_yasg import openapi
from drf_yasg.views import get_schema_view
from rest_framework import permissions


schema_view = get_schema_view(
    openapi.Info(
        title="Restaurant API",
        default_version="v1",
        description="Swagger Restaurant API documentation",
        terms_of_service="https://github.com/reakfog/restaurant_api",
        license=openapi.License(
            name="BSD 3-Clause License",
            url="https://github.com/reakfog/restaurant_api/blob/main/LICENSE",
        ),
    ),
    public=True,
    permission_classes=(permissions.AllowAny,),
)

urlpatterns = [
    re_path(r"swagger(?P<format>\.json|\.yaml)", schema_view.without_ui(cache_timeout=0), name="schema-json"),
    path(r"swagger/", schema_view.with_ui("swagger", cache_timeout=0), name="schema-swagger-ui"),
    path(r"redoc/", schema_view.with_ui("redoc", cache_timeout=0), name="schema-redoc"),
]
