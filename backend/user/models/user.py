from django.db import models
from django.contrib.auth.models import AbstractUser, Group, Permission
from transport.models import Carrier

class User(AbstractUser):
    groups = models.ManyToManyField(
        Group,
        verbose_name='groups',
        blank=True,
        help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.',
        related_name="user_set_custom",  # Zmienione related_name
        related_query_name="user_custom",
    )
    user_permissions = models.ManyToManyField(
        Permission,
        verbose_name='user permissions',
        blank=True,
        help_text='Specific permissions for this user.',
        related_name="user_set_custom",  # Zmienione related_name
        related_query_name="user_custom",
    )
    phone_number = models.CharField(max_length=15, blank=True)
    carrier = models.ForeignKey(Carrier, on_delete=models.CASCADE)


    def __str__(self):
        return self.username