from django.contrib.auth.base_user import BaseUserManager
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin
from django.db.models import BooleanField, CharField, DateTimeField, EmailField
from django.utils import timezone
from django.utils.translation import gettext_lazy as _
from restaurant_project.apps.core.utils.validators import phone_number_validator
from phonenumbers import PhoneNumberFormat, format_number, geocoder, parse

__all__ = ("User",)


class UserManager(BaseUserManager):
    def create_user(self, email, phone, password, **extra_fields):
        if not email:
            raise ValueError(_("The Email must be set"))
        if not phone:
            raise ValueError(_("The phone must be set"))
        email = self.normalize_email(email)
        user = self.model(email=email, phone=phone, **extra_fields)
        user.set_password(password)
        user.save()
        return user

    def create_admin(self, email, phone, password, **extra_fields):
        extra_fields.setdefault("is_staff", True)
        extra_fields.setdefault("is_active", True)
        if extra_fields.get("is_staff") is not True:
            raise ValueError(_("Admin must have is_staff=True."))
        return self.create_user(email, phone, password, **extra_fields)

    def create_superuser(self, email, phone, password, **extra_fields):
        extra_fields.setdefault("is_staff", True)
        extra_fields.setdefault("is_superuser", True)
        extra_fields.setdefault("is_active", True)
        if extra_fields.get("is_staff") is not True:
            raise ValueError(_("Superuser must have is_staff=True."))
        if extra_fields.get("is_superuser") is not True:
            raise ValueError(_("Superuser must have is_superuser=True."))
        return self.create_user(email, phone, password, **extra_fields)


class User(AbstractBaseUser, PermissionsMixin):
    email = EmailField(_("Email address"), max_length=500, unique=True)
    is_staff = BooleanField(_("Is staff"), default=False)
    is_active = BooleanField(_("Is active"), default=True)
    date_joined = DateTimeField(_("Date joined"), default=timezone.now)

    first_name = CharField(_("First name"), max_length=100)
    last_name = CharField(_("Last name"), max_length=100)

    phone = CharField(_("Phone number"), max_length=16, unique=True, validators=[phone_number_validator])
    country = CharField(_("Country"), max_length=100, default=None, blank=True, null=True)

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = [
        "phone",
        "first_name",
        "last_name",
    ]
    objects = UserManager()

    class Meta:
        db_table = "core_user"
        swappable = "AUTH_USER_MODEL"
        verbose_name = _("User")
        verbose_name_plural = _("Users")
        ordering = ["id"]

    def __str__(self):
        return self.email

    def save(self, *args, **kwargs):
        parsed_p_num = parse(self.phone)
        self.phone = format_number(parsed_p_num, PhoneNumberFormat.E164)
        self.country = geocoder.country_name_for_number(parsed_p_num, "en")

        super().save(*args, **kwargs)
