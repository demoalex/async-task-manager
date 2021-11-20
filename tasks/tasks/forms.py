from django.forms import ModelForm, TextInput, CharField, HiddenInput, ModelChoiceField, Select
from .models import Task


class TaskForm(ModelForm):
    reporter_str = CharField(label='Reporter email', disabled=True, required=False, )
    status_str = CharField(label='Status', disabled=True, required=False, )

    class Meta:
        model = Task
        fields = ['reporter_str', 'reporter', 'status_str', 'title', 'description']
        widgets = {
            'reporter': HiddenInput(),
        }

    @classmethod
    def status_default_str(cls):
        return str(cls._meta.model._meta.get_field('status').default)
