import uuid
from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.template.defaultfilters import truncatechars


class Task(models.Model):
    STATUS_NEW = 'new'
    STATUS_ASSIGNED = 'assigned'
    STATUS_COMPLETED = 'completed'
    STATUS_CHOICES = (
        (STATUS_NEW, 'New'),
        (STATUS_ASSIGNED, 'Assigned'),
        (STATUS_COMPLETED, 'Completed'),
    )
    public_id = models.UUIDField(default=uuid.uuid4, editable=False)
    reporter = models.ForeignKey(User, on_delete=models.CASCADE, related_name='tasks_reported')
    assignee = models.ForeignKey(User, on_delete=models.CASCADE, related_name='tasks_assigned')
    description = models.TextField(default='', blank=True)
    status = models.CharField(max_length=32, choices=STATUS_CHOICES, default=STATUS_NEW)
    created_at = models.DateTimeField(auto_now_add=True, db_index=True)
    updated_at = models.DateTimeField(auto_now=True, null=True, db_index=True, editable=False)

    def __str__(self):
        return f'#{self.id}: {self.status}: {truncatechars(self.description, 30)}'
