from django.http import HttpResponse, JsonResponse


def index(request):
    return HttpResponse("Hello, world. You're at the tasks index.")


def create_task(request):
    pass


def assign_tasks(request):
    pass

