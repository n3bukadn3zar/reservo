# -*- coding: utf-8 -*-
from django.shortcuts import render
from django.http import HttpResponse

# Import the form from users/forms.py
from .forms import StoryForm

# Import the customized User model
from .models import Story

from hackernews import HackerNews
hn = HackerNews()

def index(request):

    for story_id in hn.top_stories(limit=10):
        return HttpResponse(hn.get_item(story_id))
