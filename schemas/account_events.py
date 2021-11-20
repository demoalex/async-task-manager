from datetime import datetime
import abc
from enum import Enum
from typing import List, ClassVar, Literal, Union, Optional
from pydantic import BaseModel, ValidationError, conint


EventTypeLiteral = Literal["data_stream", "business"]


class BaseEventData(BaseModel):
    """ Should be object with fields """


class BaseEvent(BaseModel):
    event_name: str
    event_type: EventTypeLiteral
    data: BaseEventData


class TaskRoleChangedEventData(BaseEventData):
    # todo: strict type statuses to allowed enum
    # todo: strict type public_id to uuid
    public_id: str
    new_status: str
    original_status: str


class TaskRoleChangedEvent(BaseEvent):
    event_name = 'TaskRoleChanged'
    event_type: EventTypeLiteral = 'business'
    data: TaskRoleChangedEventData


# test
event_data = {
    'public_id': '67984894-e26a-4615-92f7-891ec1b9b69e',
    'new_status': 'assigned',
    'original_status': 'new'
}
e = TaskRoleChangedEvent(data=TaskRoleChangedEventData(**event_data))


class TaskCreatedUpdatedEventData(BaseEventData):
    public_id: str
    reporter: str
    assignee: str
    description: str
    status: str


class TaskCreatedEvent(BaseEvent):
    event_name = 'TaskCreated'
    event_type: EventTypeLiteral = 'data_stream'
    data: TaskCreatedUpdatedEventData


# test
event_data = {
    'public_id': '67984894-e26a-4615-92f7-891ec1b9b69e',
    'reporter': 'ee0404c5-8306-4b6b-a087-2648927fec05',
    'assignee': '8dec1f65-fc53-4484-8bef-2eeb4817be6e',
    'description': 'Style never met and those among great. '
                   'At no or september sportsmen he perfectly happiness attending. '
                   'Depending listening delivered off new she procuring satisfied sex existence. ',
    'status': 'new'
}
e = TaskCreatedEvent(data=TaskCreatedUpdatedEventData(**event_data))


class TaskUpdatedEvent(BaseEvent):
    event_name = 'TaskUpdated'
    event_type: EventTypeLiteral = 'data_stream'
    data: TaskCreatedUpdatedEventData


# test
event_data = {
    'public_id': '67984894-e26a-4615-92f7-891ec1b9b69e',
    'reporter': 'ee0404c5-8306-4b6b-a087-2648927fec05',
    'assignee': '8dec1f65-fc53-4484-8bef-2eeb4817be6e',
    'description': 'Style never met and those among great. '
                   'At no or september sportsmen he perfectly happiness attending. '
                   'Depending listening delivered off new she procuring satisfied sex existence. ',
    'status': 'new'
}
e = TaskUpdatedEvent(data=TaskCreatedUpdatedEventData(**event_data))


class TaskDeletedEventData(BaseEventData):
    public_id: str


class TaskDeletedEvent(BaseEvent):
    event_name = 'TaskDeleted'
    event_type: EventTypeLiteral = 'data_stream'
    data: TaskDeletedEventData


# test
event_data = {
    'public_id': '67984894-e26a-4615-92f7-891ec1b9b69e',
}
e = TaskDeletedEvent(data=TaskDeletedEventData(**event_data))
