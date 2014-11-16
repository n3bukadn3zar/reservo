# -*- coding: utf-8 -*-
from django.shortcuts import render
from django.http import HttpResponse

from .models import Story

def index(request):
    stories = Story.objects.order_by('score')
    return render(request, 'reader/stories.html', {'stories': stories})
