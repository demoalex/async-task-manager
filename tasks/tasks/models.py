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

    __original_status = None

    def __init__(self, *args, **kwargs):
        super(Task, self).__init__(*args, **kwargs)
        self.__original_status = self.status

    def save(self, *args, **kwargs):
        # new task
        if not self.id:
            # produce CUD event
            event = {
                'event_name': 'TaskCreated',
                'event_type': 'CUD',
                'data': {
                    'public_id': str(self.public_id),
                    'reporter': str(self.reporter.id),
                    'assignee': str(self.assignee.id),
                    'description': self.description,
                    'status': self.status
                }
            }
            topic = 'tasks-stream'
            # produce CUD event END
        else:
            # produce CUD event
            event = {
                'event_name': 'TaskUpdated',
                'event_type': 'CUD',
                'data': {
                    'public_id': str(self.public_id),
                    'reporter': str(self.reporter.id),
                    'assignee': str(self.assignee.id),
                    'description': self.description,
                    'status': self.status
                }
            }
            topic = 'tasks-stream'
            # produce CUD event END
        super(Task, self).save(*args, **kwargs)
        if self.status != self.__original_status:
            # produce Business event
            event = {
                'event_name': 'TaskRoleChanged',
                'event_type': 'business',
                'data': {
                    'public_id': str(self.public_id),
                    'new_status': self.status,
                    'original_status': self.__original_status
                }
            }
            topic = 'tasks'
            # produce Business event END

    def delete(self, *args, **kwargs):
        super(Task, self).delete(*args, **kwargs)
        # produce CUD event
        event = {
            'event_name': 'TaskDeleted',
            'event_type': 'CUD',
            'data': {
                'public_id': str(self.public_id)
            }
        }
        topic = 'tasks-stream'
        # produce CUD event END

    def __str__(self):
        return f'#{self.id}: {self.status}: {truncatechars(self.description, 30)}'
