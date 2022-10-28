# Generated by Django 4.1.2 on 2022-10-24 17:40

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Book',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=120, null=True, verbose_name='Название')),
                ('description', models.TextField(blank=True, verbose_name='Описание')),
                ('count_page', models.IntegerField(null=True, verbose_name='Количество страниц')),
                ('price', models.FloatField(null=True, verbose_name='Цена')),
                ('cover_type', models.CharField(max_length=50, null=True, verbose_name='Исполнение обложки')),
                ('cover_size', models.CharField(max_length=50, null=True, verbose_name='Оазмеры')),
                ('date_create', models.DateField(auto_now_add=True, verbose_name='Дата публикации')),
            ],
        ),
    ]
