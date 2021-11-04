from django.http import HttpResponse, JsonResponse
from django.shortcuts import render
from django.template import RequestContext
from .models import Task


def index(request):
    context = {
        'user': request.session['user']
    }
    return render(request, 'tasks/index.html', context)


def create_task(request):
    pass


def assign_tasks(request):
    pass

