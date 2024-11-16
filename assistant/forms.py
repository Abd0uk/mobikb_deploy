# forms.py
from django import forms
from .models import Topic, Case

class TopicForm(forms.Form):
    topic = forms.ModelChoiceField(queryset=Topic.objects.all(), label="Select Topic")

class CaseForm(forms.Form):
    case = forms.ModelChoiceField(queryset=Case.objects.none(), label="Select Case")

    def __init__(self, *args, **kwargs):
        topic = kwargs.pop('topic', None)
        super(CaseForm, self).__init__(*args, **kwargs)
        if topic:
            self.fields['case'].queryset = Case.objects.filter(topic=topic)
