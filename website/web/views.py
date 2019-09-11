from django.http import HttpResponse, JsonResponse
from django.shortcuts import render


def index(request):
    return HttpResponse("OK")


def weixin(request):
    print(request.GET.items())

    return HttpResponse("OK")
