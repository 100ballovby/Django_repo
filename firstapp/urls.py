# В этом файле пропишу все пути (URL-адреса) страниц приложения firstapp
from django.urls import path   # импортирую путь
from firstapp import views  # импортирую вьюшки из firstapp

urlpatterns = [
    path('', views.index, name='homepage'),  # на главной странице вызвать функцию index
    path('about', views.about),  # на странице about вызвать функцию about
    path('contacts', views.contacts),  # на странице contacts вызвать функцию contacts
]
