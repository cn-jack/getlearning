import hashlib

from datetime import datetime, timedelta

import requests

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

        return HttpResponse(WeiXin().token(signature, timestamp, nonce, echostr))
    except Exception as e:
        return HttpResponse(e)


def weixin_test(request):
    return HttpResponse(WeiXin().get())


class WeiXin():
    def __init__(self):
        self.appid = 'wx9199486083d1021c'
        self.appsecret = '56d048d91a7b218c93115f879bbf20ec'
        self._access_token = None

    def token(self, signature, timestamp, nonce, echostr):
        token = 'token'
        sha1 = hashlib.sha1()

        for x in sorted((token, timestamp, nonce)):
            sha1.update(x.encode('utf-8'))

        hashcode = sha1.hexdigest()

        if hashcode == signature:
            return echostr
        else:
            return ''

    def access_token(self):
        if self._access_token:
            if datetime.now() >= self._access_token.get('expires_time') + timedelta(seconds=self._access_token.get('expires_in')):
                self._access_token = None

        if not self._access_token:
            try:
                response = requests.get('https://api.weixin.qq.com/cgi-bin/token?grant_type=client_credential&appid=%s&secret=%s' % (self.appid, self.appsecret))

                self._access_token = response.json()
                self._access_token['expires_time'] = datetime.now()
            except:
                self._access_token = None

        return self._access_token.get('access_token')

    def get(self):
        openid = []
        next_openid = ''

        while True:
            try:
                response = requests.get('https://api.weixin.qq.com/cgi-bin/user/get?access_token=%s&next_openid=%s' % (self.access_token(), next_openid))
                data = response.json().get('data')

                openid += data.get('openid')
                next_openid = data.get('next_openid')

                if not next_openid:
                    break
            except:
                break

        return openid

# 25_5vNjeuEl9lILR1BLlS8AjlE1LjGa59zCJGdrcunHRqhyrOMZPtMpwDwwBKm5DFpJA2kEFxkiIlSnY_O1NFQgGs8zwilZrmUyVPxZ16wkTDY5ievN9TNNBQeKTFzU1WZhuJwnHhIwNDJ-h6iMMEDiADATLK