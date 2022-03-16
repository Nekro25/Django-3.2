from django.http import HttpResponse


def user_list(request):
    return HttpResponse('Список пользователей')


def user_detail(request, item):
    return HttpResponse(f'Информация о пользователе {item}')


def signup(request):
    return HttpResponse('Регистрация')


def profile(request):
    return HttpResponse('Профиль')