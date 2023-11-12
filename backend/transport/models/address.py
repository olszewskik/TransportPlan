from django.db import models


class Address(models.Model):
    street = models.CharField(max_length=255)
    city = models.CharField(max_length=100)
    postal_code = models.CharField(max_length=20)
    country = models.CharField(max_length=100)

    created = models.DateTimeField(auto_now_add=True)
    # created_by
    updated = models.DateTimeField(auto_now=True)
    # updated_by

    class Meta:
        verbose_name_plural = "Addresses"
