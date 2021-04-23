from django.db import models
from django.utils.timezone import now
from django.db.models import URLField


# Create your models here.
class Company(models.Model):
    """A model to represent the companies layer.
    This model is currently the main model of the second layer.
    These fields will represent the places that need to be tested.
    """

    class CompanyStatus(models.TextChoices):
        """
        This model is the choices for status field for Company model.
        """

        LAYOFFS = "Layoffs"
        HIRING_FREEZE = "Hiring Freeze"
        HIRING = "Hiring"

    name = models.CharField(max_length=30, unique=True)
    status = models.CharField(
        choices=CompanyStatus.choices, default=CompanyStatus.HIRING, max_length=30
    )
    last_update = models.DateTimeField(default=now, editable=True)
    application_link = URLField(blank=True)
    notes = models.CharField(max_length=100, blank=True)


    def __str__(self):
        return self.name
