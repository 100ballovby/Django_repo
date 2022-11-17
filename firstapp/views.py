from django.shortcuts import render
from django.http import HttpRequest, HttpResponse
from .forms import UserForm
# Create your views here.


def index(request):
    """
    Функция будет генерировать главную страницу ПРИЛОЖЕНИЯ
    firstapp.
    :param request: запрос на получение страницы от пользователя
    :return: текст из функци HttpResponse
    """
    userform = UserForm()
    context = {'title': 'Main page',
               'form': userform}
    return render(request, 'firstapp/index.html',
                  context=context)


def about(request):
    return HttpResponse('<h1>About page</h1>')


def contacts(request):
    return HttpResponse('<h1>Contacts</h1>')
