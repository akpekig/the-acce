import uuid

from django.contrib.auth.models import User
from django.core.exceptions import ValidationError
from django.db import models
from django.urls import reverse
from django.utils.translation import gettext_lazy as _


class Account(models.Model):
    """Model extending built-in abstract class of User model."""

    # Types of costs that the lawyer may charge.
    class UserTypes(models.IntegerChoices):
        LAWYER = 1, _("As a legal service")
        CLIENT = 2, _("As a client")

    key = models.UUIDField(default=uuid.uuid4, editable=False)
    user = models.OneToOneField(
        User,
        on_delete=models.CASCADE,
        primary_key=True,
    )
    user_type = models.IntegerField(
        choices=UserTypes.choices,
        default=UserTypes.CLIENT,
        help_text=("Select how you want to use this site."),
    )
    company = models.CharField(max_length=64, blank=True, null=True)
    email = models.EmailField(blank=True, null=True, unique=True)
    phone = models.CharField(max_length=64, blank=True, null=True, unique=True)
    website = models.CharField(max_length=128, blank=True, null=True)
    address = models.ForeignKey(
        "Location",
        models.SET_NULL,
        blank=True,
        null=True,
    )

    def get_absolute_url(self):
        """Returns the url to access a particular instance of the model."""
        return reverse("view", args=[str(self.key)])

    def clean(self):
        """Validates various fields of this model."""
        if not (self.email and self.phone and self.website and self.address):
            # Don't allow already due matters.
            raise ValidationError(
                "You need to have a way to be contacted in order to use this site!"
            )


class Location(models.Model):
    pass


class Client(models.Model):
    """Model if user is registered as a client. May convert to boolean field."""

    account = models.OneToOneField(
        Account,
        on_delete=models.CASCADE,
        primary_key=True,
    )


class Lawyer(models.Model):
    """Model if user is registered as a legal service. May convert to boolean field."""

    account = models.OneToOneField(
        Account,
        on_delete=models.CASCADE,
        primary_key=True,
    )
