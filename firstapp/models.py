from django.db import models


# Create your models here.
class Product(models.Model):
    article = models.IntegerField('Артикул', max_length=30,
                                  db_index=True)
    name = models.CharField('Название товара', max_length=100,
                            db_index=True)
    image = models.URLField('Ссылка на изображение товара',
                            default='https://cdn-icons-png.flaticon.com/512/1376/1376786.png')
    description = models.TextField('Описание товара')
    price = models.FloatField('Стоимость')
    in_stock = models.BooleanField('Товар в наличии', default=True)

    def __str__(self):  # отвечает за внешний вид записи в БД
        return f'{self.name} {self.article} | {self.price}'

    class Meta:  # настройка отображения вашей модели в административной панели Django
        ordering = ['article', 'name',]  # фильтрация объектов в административной панели
        verbose_name = 'Товар'  # название объекта в административной панели
        verbose_name_plural = 'Товары'  # название раздела с сущностями в админке




