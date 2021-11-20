from .common import BaseEvent, BaseEventData, EventTypeLiteral


class TaskStatusChangedEventData(BaseEventData):
    # todo: strict type statuses to allowed enum
    # todo: strict type public_id to uuid
    public_id: str
    new_status: str
    original_status: str


class TaskStatusChangedEvent(BaseEvent):
    event_name = 'TaskRoleChanged'
    event_type: EventTypeLiteral = 'business'
    data: TaskStatusChangedEventData


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


class TaskUpdatedEvent(BaseEvent):
    event_name = 'TaskUpdated'
    event_type: EventTypeLiteral = 'data_stream'
    data: TaskCreatedUpdatedEventData


class TaskDeletedEventData(BaseEventData):
    public_id: str


class TaskDeletedEvent(BaseEvent):
    event_name = 'TaskDeleted'
    event_type: EventTypeLiteral = 'data_stream'
    data: TaskDeletedEventData
