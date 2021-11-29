import uuid
from datetime import date
from decimal import Decimal
from django.core.exceptions import ValidationError
from django.core.validators import MinValueValidator, MaxValueValidator
from django.db import models
from django.urls import reverse
from django.utils.translation import gettext_lazy as _

# Human-readable limits for positive integers.
POSITIVE_DECIMAL_VALIDATORS = [
    MinValueValidator(Decimal('0.00')), 
    MaxValueValidator(Decimal('9999.99')),
]

class Matter(models.Model):
    """Model representing a matter: a transaction between lawyer and client and/or the task a lawyer must carry out for the client."""
    # Types of costs that the lawyer may charge.
    class CostTypes(models.TextChoices):
        PRICE = 'P', _('Price')
        RATE = 'R', _('Rate')

    key = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    title = models.CharField(max_length=64, help_text="Enter the title of the matter. Keep it short.")
    description = models.CharField(max_length=512, help_text="Describe the matter. Don't make it complex.")
    cost_type = models.CharField(max_length=1, choices=CostTypes.choices, default=CostTypes.PRICE, 
                                help_text=('Select the type of cost you will charge.'))
    amount = models.DecimalField(max_digits=6, decimal_places=2, validators=POSITIVE_DECIMAL_VALIDATORS, default=0, 
                                help_text="Include all costs related to the matter.")
    estimated_hours = models.DecimalField(max_digits=6, decimal_places=2, validators=POSITIVE_DECIMAL_VALIDATORS, default=5,
                                help_text=('Approximate how many hours you will work.'))
    logged_hours = models.DecimalField(max_digits=6, decimal_places=2, validators=POSITIVE_DECIMAL_VALIDATORS, default=0,
                                help_text=('Approximate how many hours you have worked. ' 
                                    'This can not exceed estimated hours without your client\'s permission.'))
    start_date = models.DateField(default=date.today, help_text=('When should the client expect you to start working?'))
    due_date = models.DateField(blank=True, null=True)
    has_client_permission = models.BooleanField("Do you have your client's explicit permission to begin immediately?", default=False)
    has_external_services = models.BooleanField("Do you need to involve external services in this matter?", default=False)
    has_client_pre_tasks = models.BooleanField("Does the client need to carry out any tasks before you begin?", default=False)
    has_related_articles = models.BooleanField("Does the client need to know any extra information?", default=False)
    is_changeable = models.BooleanField("Do you want to change the cost in the future?", default=False)
    is_active = models.BooleanField(default=True)
    lawyer_key = models.ForeignKey(
        'Lawyer',
        models.CASCADE,
    )
    client_key = models.ForeignKey(
        'Client',
        models.CASCADE,
    )

    class Meta:
        # Order alphabetically by title
        ordering = ['title']

    def __str__(self):
        """Returns human-readable reference to model instance."""
        return self.title

    def get_absolute_url(self):
        """Returns the url to access a particular instance of the model."""
        return reverse('view', args=[str(self.key)])
    
    def clean(self):
        """Validates various fields of this model."""
        if not self.has_client_permission:
            # Don't allow matters to begin without client permission to share involve external services or carry out pre-tasks.
            if self.has_client_pre_tasks:
                raise ValidationError('You must check in with your client if they have tasks to do before you can start!')
            elif self.has_external_services:
                raise ValidationError('You must check in with your client before sharing their information with external services!')
            # Don't allow client to be charged for work that they haven't permitted.
            elif self.logged_hours or (self.start_date < date.today()):
                raise ValidationError('You can not have started without your client\'s permission. '
                                    'Any work done without permission can not be logged nor charged!')

class Lawyer(models.Model):
    pass
class Client(models.Model):
    pass