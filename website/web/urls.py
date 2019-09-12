from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('weixin_token', views.weixin_token, name='weixin_token'),
    path('weixin_test', views.weixin_test, name='weixin_test'),
]
