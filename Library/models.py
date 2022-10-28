from django.db import models


class Book(models.Model):
    name = models.CharField(max_length=120, null=True, verbose_name='Название')
    description = models.TextField(blank=True, null=False, verbose_name='Описание')
    count_page = models.IntegerField(null=True, verbose_name='Количество страниц')
    price = models.FloatField(null=True, verbose_name='Цена')
    cover_type = models.CharField(max_length=50, null=True, verbose_name='Исполнение обложки')
    cover_size = models.CharField(max_length=50, null=True, verbose_name='Оазмеры')
    date_create = models.DateField(auto_now_add=True, verbose_name='Дата публикации')

