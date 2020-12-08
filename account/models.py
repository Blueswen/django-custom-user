from django.contrib.auth.models import AbstractUser
from django.db import models


class CustomUser(AbstractUser):
    birthday = models.DateField(null=True, blank=True, default=None)
    # add additional fields in here

    def __str__(self):
        return self.username
