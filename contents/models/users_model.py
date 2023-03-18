from django.contrib.auth.models import AbstractUser
from django.db import models
from uuid import uuid4


class User(AbstractUser):
    uuid = models.UUIDField(default=uuid4(), editable=False, null=True, blank=True)

