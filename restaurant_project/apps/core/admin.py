from django.contrib.admin import ModelAdmin, register
from restaurant_project.apps.core.models import User


@register(User)
class UserAdmin(ModelAdmin):
    pass