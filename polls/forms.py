from dataclasses import field
from django import forms
from .models import Question,Topic
class QuestionForm(forms.Form):
    class Meta:
        model=Question
        fields="__all__"
    