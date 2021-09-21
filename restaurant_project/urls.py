from django.contrib import admin
from django.urls import include, path

from restaurant_project.yasg import urlpatterns as doc_urls


urlpatterns = [
    path("admin/", admin.site.urls),
    path("auth/", include("djoser.urls")),
    path("auth/", include("djoser.urls.jwt")),
    path("api/v1/", include("restaurant_project.apps.api.urls")),
]

urlpatterns += doc_urls
