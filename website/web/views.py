import hashlib

from django.http import HttpResponse, JsonResponse
from django.shortcuts import render


def index(request):
    return HttpResponse("OK")


def weixin_token(request):
    try:
        signature = request.GET.get('signature')
        timestamp = request.GET.get('timestamp')
        nonce = request.GET.get('nonce')
        echostr = request.GET.get('echostr')

        token = 'token'
        sha1 = hashlib.sha1()

        for x in sorted((token, timestamp, nonce)):
            sha1.update(x)

        hashcode = sha1.hexdigest()

        if hashcode == signature:
            return HttpResponse(echostr)
        else:
            return HttpResponse('')
    except Exception as e:
        return HttpResponse(e)
