from django.http import HttpResponse


def item_list(request):
    return HttpResponse('список предметов')


def item_detail(request, item):
    return HttpResponse(f'Информация о предмете {item}')
