from django import forms
from django.forms import widgets
from .models import Topic, Entry

class TopicForm(forms.ModelForm):
    """ Build forms to enter the information by the user."""
    class Meta:
        model = Topic
        fields = ['text']
        labels = {'text': ''}

class EntryForm(forms.ModelForm):
    class Meta:
        model = Entry
        fields = ['text']
        labels = {'text': 'Entry:'}
        widgets = {'text': forms.Textarea(attrs={'cols': 80})}