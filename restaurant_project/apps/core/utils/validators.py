from django.core.exceptions import ValidationError
from django.utils.translation import gettext_lazy as _
from phonenumbers import is_valid_number, parse

__all__ = ("phone_number_validator",)


def phone_number_validator(phone_number: str) -> None:
    try:
        parsed_p_num = parse(phone_number)
        is_valid_number(parsed_p_num)
    except:
        raise ValidationError(_(f"{phone_number} is not a correct phone number."))
