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
    context = {'title': 'Main page'}
    return render(request, 'firstapp/index.html',
                  context=context)


def about(request):
    return HttpResponse('<h1>About page</h1>')


def contacts(request):
    return HttpResponse('<h1>Contacts</h1>')