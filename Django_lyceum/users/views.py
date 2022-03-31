from django.shortcuts import render


def user_list(request):
    template = 'users/user_list.html'
    return render(request, template)


def user_detail(request, item):
    template = 'user/user_detail.html'
    return render(request, template)


def signup(request):
    template = 'user/signup.html'
    return render(request, template)


def profile(request):
    template = 'user/profile.html'
    return render(request, template)
