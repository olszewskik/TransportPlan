from django.db import models


class Carrier(models.Model):
    name = models.CharField(max_length=100, unique=True)
    phone_no = models.CharField(max_length=20)
    email = models.EmailField(max_length=250)

    created = models.DateTimeField(auto_now_add=True)
    # created_by
    updated = models.DateTimeField(auto_now=True)
    # updated_by

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = "Carriers"
