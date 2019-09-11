import hashlib

from django.http import HttpResponse, JsonResponse
from django.shortcuts import render


def index(request):
    return HttpResponse("OK")


def weixin_token(request):
    try:
        signature = request.GET['signature']
        timestamp = request.GET['timestamp']
        nonce = request.GET['nonce']
        echostr = request.GET['echostr']

        token = 'token'
        sha1 = hashlib.sha1()

        for x in sorted((token, timestamp, nonce)):
            sha1.update(x)

        hashcode = sha1.hexdigest()

        if hashcode == signature:
            return echostr
        else:
            return ''
    except Exception as e:
        return e
