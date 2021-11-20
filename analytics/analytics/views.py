from django.http import HttpResponse, JsonResponse
from django.shortcuts import render
from django.template import RequestContext


def index(request):
    context = {
        'title': 'Analytics',
    }
    return HttpResponse("Hello, world. You're at the analytics index.")
