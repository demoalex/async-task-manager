from rele import sub
from .models import ExternalUser


@sub(topic='accounts-stream')
def accounts_stream(data, **kwargs):
    print(data)
    try:
        account_obj = data['data']
        if data['event_name'] == 'AccountCreated':
            ExternalUser.objects.create(**account_obj)
        elif data['event_name'] == 'AccountUpdated':
            try:
                external_user = ExternalUser.objects.get(public_id=account_obj['public_id'])
                external_user.public_id = account_obj['public_id']
                external_user.username = account_obj['username']
                external_user.full_name = account_obj['full_name']
                external_user.email = account_obj['email']
                external_user.role = account_obj['role']
                external_user.save()
            except ExternalUser.DoesNotExist:
                ExternalUser.objects.create(**account_obj)
        elif data['event_name'] == 'AccountDeleted':
            try:
                ExternalUser.objects.get(public_id=account_obj['public_id']).delete()
            except ExternalUser.DoesNotExist:
                pass
    except KeyError:
        print('Incorrect account message.')
