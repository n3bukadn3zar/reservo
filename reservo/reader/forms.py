# -*- coding: utf-8 -*-
from django import forms

from reader.models import Story


class StoryForm(forms.ModelForm):

    title = forms.CharField()
    url = forms.CharField()
    score = forms.CharField()
    submitter = forms.CharField()
    timestamp = forms.CharField()

    class Meta:
        # Set this form to use the User model.
        model = Story

        # Constrain the UserForm to just these fields.
        fields = ("title", "url", "score", "submitter", "timestamp")
