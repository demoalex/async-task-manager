import uuid
from django.db import models


class ExternalUser(models.Model):
    public_id = models.UUIDField(default=uuid.uuid4, editable=False)
    username = models.CharField(max_length=150, blank=True, editable=False)
    full_name = models.CharField(max_length=255, blank=True, editable=False)
    email = models.EmailField(max_length=255, blank=True, editable=False)
    role = models.CharField(max_length=32, blank=True, editable=False)
    created_at = models.DateTimeField(auto_now_add=True, db_index=True)
    updated_at = models.DateTimeField(auto_now=True, null=True, db_index=True, editable=False)

    def __str__(self):
        return f'#{self.public_id}: {self.email}'
