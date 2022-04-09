from django.shortcuts import render

from constants import USER_DETAIL_TEMPLATE, USER_LIST_TEMPLATE, \
    USER_SIGNUP_TEMPLATE, USER_PROFILE_TEMPLATE


def user_list(request):
    template = USER_LIST_TEMPLATE
    return render(request, template)


def user_detail(request, item):
    template = USER_DETAIL_TEMPLATE
    return render(request, template)


def signup(request):
    template = USER_SIGNUP_TEMPLATE
    return render(request, template)


def profile(request):
    template = USER_PROFILE_TEMPLATE
    return render(request, template)
