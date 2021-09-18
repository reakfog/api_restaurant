from typing import Union

from django.db.models import DateTimeField, Model


class TimestampedModel(Model):
    """
    Based on https://github.com/jazzband/django-model-utils/blob/master/model_utils/models.py TimeStampedModel
    An abstract base class model that provides self-updating ``created_at`` and ``updated_at`` fields.
    Tested in tests/product/models/test_batch.py test_save_without_updated_at_in_update_fields
    """

    created_at = DateTimeField(auto_now_add=True)
    updated_at = DateTimeField(auto_now=True)

    class Meta:
        abstract = True

    def save(
        self,
        force_insert: bool = False,
        force_update: bool = False,
        using: str = None,
        update_fields: Union[list, tuple, set] = None,
    ) -> None:
        if update_fields:
            if not isinstance(update_fields, set):
                update_fields = set(update_fields)
            update_fields = update_fields.union({"updated_at"})
        super().save(force_insert, force_update, using, update_fields)
