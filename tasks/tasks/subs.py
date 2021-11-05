from rele import sub


@sub(topic='tasks-stream')
def tasks_stream(data, **kwargs):
    print(data)


@sub(topic='tasks')
def tasks(data, **kwargs):
    print(data)


@sub(topic='accounts-stream')
def accounts_stream(data, **kwargs):
    print(data)


@sub(topic='accounts')
def accounts(data, **kwargs):
    print(data)
