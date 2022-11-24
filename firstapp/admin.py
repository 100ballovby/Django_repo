from django.contrib import admin
from .models import Product
# Register your models here.


class ProductAdmin(admin.ModelAdmin):
    # данные, которые отображаются в списке сущностей в админке
    list_display = ('article', 'name', 'price', 'in_stock',)
    # по каким данным буду фильтровать элементы
    list_filter = ('in_stock',)
    # некоторые поля элементов можно менять прямо из общего списка
    list_editable = ('price', 'in_stock',)
    # критерий поиска
    search_fields = ('article', 'name',)

admin.site.register(Product, ProductAdmin)  # отображаю в админке новую модель
