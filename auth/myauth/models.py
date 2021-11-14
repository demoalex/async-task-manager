import uuid
import rele
from django.db import models
from django.contrib.auth.models import AbstractUser


class MyUser(AbstractUser):
    ROLE_ADMIN = 'admin'
    ROLE_MANAGER = 'manager'
    ROLE_ACCOUNTANT = 'accountant'
    ROLE_DEVELOPER = 'developer'
    ROLE_CHOICES = (
        (ROLE_ADMIN, 'Administrator'),
        (ROLE_MANAGER, 'Manager'),
        (ROLE_ACCOUNTANT, 'Accountant'),
        (ROLE_DEVELOPER, 'Developer'),
    )
    public_id = models.UUIDField(default=uuid.uuid4, editable=False)
    role = models.CharField(max_length=32, choices=ROLE_CHOICES, default=ROLE_DEVELOPER)

    __original_role = None

    def get_full_name(self):
        return ' '.join([self.first_name, self.last_name])

    def __init__(self, *args, **kwargs):
        super(MyUser, self).__init__(*args, **kwargs)
        self.__original_role = self.role

    def save(self, *args, **kwargs):
        # new account
        if not self.id:
            # produce CUD event
            event = {
                'event_name': 'AccountCreated',
                'event_type': 'CUD',
                'data': {
                    'public_id': str(self.public_id),
                    'username': str(self.username),
                    'email': self.email,
                    'full_name': self.get_full_name(),
                    'role': self.role
                }
            }
            topic = 'accounts-stream'
            rele.publish(topic, event)
            # produce CUD event END
        else:
            # produce CUD event
            event = {
                'event_name': 'AccountUpdated',
                'event_type': 'CUD',
                'data': {
                    'public_id': str(self.public_id),
                    'username': str(self.username),
                    'email': self.email,
                    'full_name': self.get_full_name(),
                    'role': self.role
                }
            }
            topic = 'accounts-stream'
            rele.publish(topic, event)
            # produce CUD event END
        super(MyUser, self).save(*args, **kwargs)
        if self.role != self.__original_role:
            # produce Business event
            event = {
                'event_name': 'AccountRoleChanged',
                'event_type': 'business',
                'data': {
                    'public_id': str(self.public_id),
                    'new_role': self.role,
                    'original_role': self.__original_role
                }
            }
            topic = 'accounts'
            rele.publish(topic, event)
            # produce Business event END

    def delete(self, *args, **kwargs):
        super(MyUser, self).delete(*args, **kwargs)
        # produce CUD event
        event = {
            'event_name': 'AccountDeleted',
            'event_type': 'CUD',
            'data': {
                'public_id': str(self.public_id)
            }
        }
        topic = 'accounts-stream'
        print(event)
        rele.publish(topic, event)
        # produce CUD event END
