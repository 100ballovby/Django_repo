from django.shortcuts import render
from django.http import HttpRequest, HttpResponse
# Create your views here.


def index(request):
    """
    Функция будет генерировать главную страницу ПРИЛОЖЕНИЯ
    firstapp.
    :param request: запрос на получение страницы от пользователя
    :return: текст из функци HttpResponse
    """
    return HttpResponse('Hello! There is my site!')
