from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect

from .models import Fruit
from .forms import FruitForm


def index(request):
    print(request)
    return HttpResponse('Hello Django')


def fruit(request):
    fruits = Fruit.objects.all()  # Возврат всех записей из БД
    response = '<h1>Список фруктов</h1>'
    for item in fruits:
        response += f'<div>\n<p>{item.name}</p>\n<p>{item.price}</p></div>'
    # responce += '<h2>Pear</h2>'
    # responce += '<h3>Banan</h3>'
    # responce += '<h4>Avocado</h4>'
    return HttpResponse(response)


def index_template(request):
    return render(request, 'fruit/index.html')


def fruit_template(request):
    context = {'title': 'Фрукты'}

    fruits = Fruit.objects.all()
    context['fruit_list'] = fruits

    if request.method == "GET":
        fruit_id = request.GET.get('id', 1)
        try:
            fruit_one = Fruit.objects.get(pk=fruit_id)
        except:
            pass
        else:
            context['fruit_one'] = fruit_one

        context['name'] = request.GET.get('name', 'banan')
    elif request.method == "POST":
        fruit_id = request.POST.get('id', 1)
        try:
            fruit_one = Fruit.objects.get(pk=fruit_id)
        except:
            pass
        else:
            context['fruit_one'] = fruit_one

        context['name'] = request.POST.get('name', 'banan')

    # context = {
    #     'title': 'Фрукты',
    #     'fruit_list': fruits,
    #     'fruit_one': fruit_one,
    #     'name': name
    # }
    return render(
        request=request,
        template_name='fruit/fruit-all.html',
        context=context
    )


def fruit_add(request):
    if request.method == "POST":
        context = dict()
        context['name'] = request.POST.get('name')
        context['description'] = request.POST.get('description')
        context['price'] = request.POST.get('price')
        context['date_expired'] = request.POST.get('date_expired')
        context['photo'] = request.POST.get('photo')

        Fruit.objects.create(
            name=context['name'],
            description=context['description'],
            price=context['price'],
            date_expired=context['date_expired'],
            photo=context['photo'],
        )

        return HttpResponseRedirect('/fruit/fruitsList/')
    else:
        fruitform = FruitForm()
        context = {'form': fruitform}
        return render(request, 'fruit/fruit-add.html', context=context)


def fruit_detail(request, fruit_id):
    # fruit = Fruit.objects.get(pk=fruit_id)
    fruit = get_object_or_404(Fruit, pk=fruit_id)
    # context = dict()
    # context['fruit_item'] = fruit
    return render(request, 'fruit/fruit-info.html', {'fruit_item': fruit})


def request_info(request):
    if request.GET.get("META") == "TRUE":
        meta_output = ""
        for key, value in request.META.items():
            meta_output += f'{key}: {value}<br>'
        return HttpResponse(meta_output)
    return render(request, 'info/request.html', {'req_item': request})
