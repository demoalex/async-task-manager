import uuid
import json
import rele
from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.template.defaultfilters import truncatechars

import sys
sys.path.append('..')
from schemas.tasks_events import (TaskCreatedEvent, TaskUpdatedEvent, TaskCreatedUpdatedEventData,
                                  TaskDeletedEvent, TaskDeletedEventData,
                                  TaskStatusChangedEvent, TaskStatusChangedEventData, )


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
    reporter = models.ForeignKey(ExternalUser, on_delete=models.CASCADE, related_name='tasks_reported')
    assignee = models.ForeignKey(ExternalUser, on_delete=models.CASCADE, related_name='tasks_assigned', null=True)
    title = models.CharField(max_length=255, default='', blank=True, )
    description = models.TextField(default='', blank=True, )
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
            event_data = {
                'public_id': str(self.public_id),
                'reporter': str(self.reporter.public_id),
                'assignee': str(self.assignee.public_id) if self.assignee else None,
                'description': self.description,
                'status': self.status
            }
            event = TaskCreatedEvent(data=TaskCreatedUpdatedEventData(**event_data))
            topic = 'tasks-stream'
            rele.publish(topic, event.json())
            # produce CUD event END
            self.assign_task_no_save()
        else:
            # produce CUD event
            event_data = {
                'public_id': str(self.public_id),
                'reporter': str(self.reporter.public_id),
                'assignee': str(self.assignee.public_id) if self.assignee else None,
                'description': self.description,
                'status': self.status
            }
            event = TaskUpdatedEvent(data=TaskCreatedUpdatedEventData(**event_data))
            topic = 'tasks-stream'
            rele.publish(topic, event.json())
            # produce CUD event END
        super(Task, self).save(*args, **kwargs)
        if self.status != self.__original_status:
            # produce Business event
            event_data = {
                'public_id': str(self.public_id),
                'new_status': self.status,
                'original_status': self.__original_status
            }
            event = TaskStatusChangedEvent(data=TaskStatusChangedEventData(**event_data))
            topic = 'tasks'
            rele.publish(topic, event.json())
            # produce Business event END

    def delete(self, *args, **kwargs):
        super(Task, self).delete(*args, **kwargs)
        # produce CUD event
        event_data = {
            'public_id': str(self.public_id)
        }
        event = TaskDeletedEvent(data=TaskDeletedEventData(**event_data))
        topic = 'tasks-stream'
        rele.publish(topic, event.json())
        # produce CUD event END

    def assign_task_no_save(self, ):
        # kill! prod server with .order_by('?')
        self.assignee = ExternalUser.objects.filter(role='developer').order_by('?').first()
        self.status = Task.STATUS_ASSIGNED
        # self.save()

    @classmethod
    def reassign_tasks(cls):
        queryset = cls.objects.filter(status__in=[cls.STATUS_ASSIGNED, cls.STATUS_NEW])
        for task in queryset:
            task.assign_task_no_save()
            task.save()

    @property
    def short_description(self):
        return truncatechars(self.description, 30)

    def __str__(self):
        return f'#{self.id}: {self.status}: {self.short_description}'
