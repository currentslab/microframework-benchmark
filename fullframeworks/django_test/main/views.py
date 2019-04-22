from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from django_test.settings import JSON_DATA, TEXT


def text_view(request):
    return HttpResponse(TEXT)

def json_view(request):
    return JsonResponse(JSON_DATA)

