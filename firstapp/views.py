from django.shortcuts import render
from django.http import HttpRequest, HttpResponse
from .forms import UserForm
from .models import Product
# Create your views here.


def index(request):
    products = Product.objects.all()  # достать все продукты
    print(products)
    return render(request, 'firstapp/index.html', {
        'title': 'Главная страница',
        'prod': products,
    })


def about(request):
    return HttpResponse('<h1>About page</h1>')


def contacts(request):
    """
        Функция будет генерировать главную страницу ПРИЛОЖЕНИЯ
        firstapp.
        :param request: запрос на получение страницы от пользователя
        :return: текст из функци HttpResponse
        """
    if request.method == 'POST':
        name = request.POST.get('name')  # получаю инфу по имени поля
        age = request.POST.get('age')
        output = f'<h1>Client</h1><h2>Name - {name}</h2><h3>Age - {age}</h3>'
        return HttpResponse(output)
    else:
        userform = UserForm(label_suffix='?')  # у каждой подписи в конце вместо : будет стоять ?
        context = {'title': 'Main page',
                   'form': userform}
        return render(request, 'firstapp/index.html',
                      context=context)