from .common import BaseEvent, BaseEventData, EventTypeLiteral


class AccountRoleChangedEventData(BaseEventData):
    public_id: str
    new_role: str
    original_role: str


class AccountRoleChangedEvent(BaseEvent):
    event_name = 'AccountRoleChanged'
    event_type: EventTypeLiteral = 'business'
    data: AccountRoleChangedEventData


# test
event_data = {
    'public_id': 'ee0404c5-8306-4b6b-a087-2648927fec05',
    'new_role': 'manager',
    'original_role': 'accountant'
}
e = AccountRoleChangedEvent(data=AccountRoleChangedEventData(**event_data))


class AccountCreatedUpdatedEventData(BaseEventData):
    public_id: str
    username: str
    email: str
    full_name: str
    role: str


class AccountCreatedEvent(BaseEvent):
    event_name = 'AccountCreated'
    event_type: EventTypeLiteral = 'data_stream'
    data: AccountCreatedUpdatedEventData


# test
event_data = {
    'public_id': 'ee0404c5-8306-4b6b-a087-2648927fec05',
    'username': 'someuser',
    'email': 'user@email.com',
    'full_name': 'Alex Lexi',
    'role': 'developer'
}
e = AccountCreatedEvent(data=AccountCreatedUpdatedEventData(**event_data))


class AccountUpdatedEvent(BaseEvent):
    event_name = 'AccountUpdated'
    event_type: EventTypeLiteral = 'data_stream'
    data: AccountCreatedUpdatedEventData


# test
event_data = {
    'public_id': 'ee0404c5-8306-4b6b-a087-2648927fec05',
    'username': 'someuser',
    'email': 'user@email.com',
    'full_name': 'Alex Lexi',
    'role': 'manager'
}
e = AccountUpdatedEvent(data=AccountCreatedUpdatedEventData(**event_data))


class AccountDeletedEventData(BaseEventData):
    public_id: str


class AccountDeletedEvent(BaseEvent):
    event_name = 'AccountDeleted'
    event_type: EventTypeLiteral = 'data_stream'
    data: AccountDeletedEventData


# test
event_data = {
    'public_id': 'ee0404c5-8306-4b6b-a087-2648927fec05',
}
e = AccountDeletedEvent(data=AccountDeletedEventData(**event_data))
