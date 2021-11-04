import uuid
from django.db import models
from django.contrib.auth.models import AbstractUser


class MyUser(AbstractUser):
    public_id = models.UUIDField(default=uuid.uuid4, editable=False)
