from django.http import HttpResponse


def index(request):
    return HttpResponse("Index")


def error(request):
    1/0
