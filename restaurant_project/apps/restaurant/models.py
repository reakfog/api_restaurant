from django.conf import settings
from django.db.models import SET_NULL, CharField, ForeignKey, SlugField, URLField
from django.utils.translation import gettext_lazy as _
from restaurant_project.apps.utils.models import TimestampedModel


class Restaurant(TimestampedModel):
    user = ForeignKey(settings.AUTH_USER_MODEL, on_delete=SET_NULL, related_name="restaurant", null=True)

    name = SlugField(_("Name"), max_length=100)
    description = CharField(_("Description"), max_length=1000, blank=True, null=True, default=None)
    link = URLField(_("Link"), blank=True, null=True, default=None)

    class Meta:
        db_table = "restaurant_restaurant"
        verbose_name = _("Restaurant")
        verbose_name_plural = _("Restaurants")
        ordering = ["id"]
