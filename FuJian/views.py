from django.shortcuts import render

import datetime
from django.http import HttpResponse
# Create your views here.

def index(request):
    return HttpResponse('hello')

def current_datetime(request):
    now = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    return HttpResponse('Current Datetime: %s' % now)
