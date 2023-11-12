from django.db import models


class Customer(models.Model):
    name = models.CharField(max_length=100, unique=True)

    created = models.DateTimeField(auto_now_add=True)
    # created_by
    updated = models.DateTimeField(auto_now=True)
    # updated_by

    def __str__(self):
        return self.name
