from django.urls import path
from . import views  # из каталога приложения импортировать файл views

urlpatterns = [
    path('', views.user_home, name='account')
]
