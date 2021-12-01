import uuid
from datetime import date
from decimal import Decimal

from django.core.exceptions import ValidationError
from django.core.validators import MaxValueValidator, MinValueValidator
from django.db import models
from django.urls import reverse
from django.utils.translation import gettext_lazy as _

# Human-readable limits for positive integers.
POSITIVE_DECIMAL_VALIDATORS = [
    MinValueValidator(Decimal("0.00")),
    MaxValueValidator(Decimal("9999.99")),
]


class Negotiation(models.Model):
    """Model representing a negotiation of fees between lawyer and client."""

    # Types of costs that the lawyer may charge.
    class CostTypes(models.TextChoices):
        PRICE = "P", _("Price")
        RATE = "R", _("Rate")

    key = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    title = models.CharField(
        max_length=64, help_text="Enter a short, memorable title."
    )
    cost_type = models.CharField(
        max_length=1,
        choices=CostTypes.choices,
        default=CostTypes.PRICE,
        help_text=("Select the type of cost you will charge."),
    )
    amount = models.DecimalField(
        max_digits=6,
        decimal_places=2,
        validators=POSITIVE_DECIMAL_VALIDATORS,
        default=0,
        help_text="Include the base cost for hiring you.",
    )
    initial_amount = models.DecimalField(
        max_digits=6,
        decimal_places=2,
        validators=POSITIVE_DECIMAL_VALIDATORS,
        default=0,
        help_text="How much of the base cost must be paid before you begin work?.",
    )
    budget = models.DecimalField(
        max_digits=6,
        decimal_places=2,
        validators=POSITIVE_DECIMAL_VALIDATORS,
        default=100,
        help_text="Set the limit for spending on the base cost.",
    )
    is_accepted = models.BooleanField(
        "Do you want to accept the offer?", default=False
    )
    is_changeable = models.BooleanField(
        "Do you want to change the cost in the future?", default=False
    )
    lawyer_key = models.ForeignKey(
        "Lawyer",
        models.CASCADE,
    )
    client_key = models.ForeignKey(
        "Client",
        models.CASCADE,
    )

    class Meta:
        # Order alphabetically by title
        ordering = ["title"]

    def __str__(self):
        """Returns human-readable reference to model instance."""
        return self.title

    def get_absolute_url(self):
        """Returns the url to access a particular instance of the model."""
        return reverse("view", args=[str(self.key)])

    def clean(self):
        """Validates various fields of this model."""
        if self.initial_amount  > self.amount:
            raise ValidationError(
                "The client can't pay more than your base rate!"
            )

class Lawyer(models.Model):
    pass


class Client(models.Model):
    pass
