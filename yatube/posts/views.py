from django.shortcuts import render

# Create your views here.

from django.http import HttpResponse
from django.shortcuts import render
from .models import Post


def index(request):
    # Одна строка вместо тысячи слов на SQL:
    # в переменную posts будет сохранена выборка из 10 объектов модели Post,
    # отсортированных по полю pub_date по убыванию (от больших значений к меньшим)
    # В функции index() переменная posts получает выборку записей модели
    # Post из БД. После имени модели и специальной точки входа .objects указаны условия запроса.
    # сортируем записи по свойству pub_date по убыванию, от больших
    # значений к меньшим (об этом говорит знак -): новые записи оказываются вверху выборки
    # в выборку попадут только первые 10 элементов из полученного списка.
    posts = Post.objects.order_by('-pub_date')[:10]
    # В словаре context отправляем информацию в шаблон
    context = {
        'posts': posts,
    }
    return render(request, 'posts/index.html', context)


def group_list(request):
    template = 'posts/group_list.html'
    return render(request, template)



