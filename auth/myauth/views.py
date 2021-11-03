from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from django.template import RequestContext


@login_required
def logged_in(request):
    context = {}
    return render(request, 'myauth/logged_in.html', context)
