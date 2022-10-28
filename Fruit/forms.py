from django import forms


class FruitForm(forms.Form):
    name = forms.CharField(
        max_length=50,
        min_length=2,
        strip=True,
        label='Название фрукта')
    description = forms.CharField(
        max_length=150,
        min_length=2,
        strip=True,
        label='Описание фрукта',
        widget=forms.Textarea,
        initial="Описание")
    price = forms.FloatField(
        min_value=1,
        # step_size=10,
        label='Цена фрукта',
        initial=40)
    date_expired = forms.DateField(
        label='Дата просрочки фрукта',
        # widget=forms.SelectDateWidget,
        help_text='Укажите дату просрочки указанную на упаковке')
    photo = forms.ImageField(
        required=False,
        label='Фотография фрукта')

    # Валидация
    # required=True - обязательное поле
    # max_length - максимальная длина текста
    # min_length - минимальная длина текста
    # max_value - максимальное значение числа
    # max_value - минимальное значение числа
    # step_size - шаг при установки числового значения

    # Стили
    # label - Вывод названия
    # widget - Указания типа поля
    # initial - Значение по умолчанию
    # help_text - подсказка под полем

