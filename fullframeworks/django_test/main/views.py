from django.shortcuts import render
from django.http import HttpResponse
from django_test.settings import JSON_DATA, TEXT
import ujson as json


def text_view(request):
    return HttpResponse(TEXT)

def json_view(request):
    serialized = json.dumps(JSON_DATA)
    return HttpResponse(serialized, content_type='application/json')

