from django.db import models
from django.utils.translation import gettext_lazy as _
from .carrier import Carrier


class Transport(models.Model):
    class TransportStatus(models.TextChoices):
        PLANNED = "PLN", _("Planned")
        CONFIRMED = "CNF", _("Confirmed")
        REALIZED = "RLZ", _("Realized")
        UNREALIZED = "UNR", _("Unrealized")

    class TransportType(models.TextChoices):
        LOADING = "LDG", _("Loading")
        UNLOADING = "ULD", _("Unloading")

    status = models.CharField(
        max_length=3, choices=TransportStatus.choices, default=TransportStatus.PLANNED
    )
    transport_type = models.CharField(
        max_length=3, choices=TransportType.choices, default=TransportType.LOADING
    )
    date = models.DateField()
    time = models.TimeField()
    carrier = models.ForeignKey(Carrier, on_delete=models.CASCADE)

    description = models.TextField()

    created = models.DateTimeField(auto_now_add=True)
    # created_by
    updated = models.DateTimeField(auto_now=True)
    # updated_by
