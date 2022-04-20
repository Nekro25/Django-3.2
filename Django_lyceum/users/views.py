from django import forms
from django.contrib.auth import get_user_model, get_user
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render, redirect, get_object_or_404

from constants import USER_DETAIL_TEMPLATE, USER_LIST_TEMPLATE, \
    USER_SIGNUP_TEMPLATE, USER_PROFILE_TEMPLATE
from rating.models import Rating
from .models import Profile

User_model = get_user_model()


def user_list(request):
    template = USER_LIST_TEMPLATE
    users = User_model.objects.values('username')
    context = {
        'users': users
    }
    return render(request, template, context=context)


def user_detail(request, item):
    template = USER_DETAIL_TEMPLATE
    user = get_object_or_404(Profile.objects.select_related('user').only(
        'birthday', 'user__email', 'user__first_name', 'user__last_name',
        'user__username'), pk=item)
    items = Rating.objects.filter(user__id=item, star=5).select_related(
        'item').select_related('user').only('user__id', 'star', 'item__name')
    context = {
        'user': user,
        'items': items,
    }
    return render(request, template, context=context)


def signup(request):
    template = USER_SIGNUP_TEMPLATE
    form = UserCreationForm(request.POST or None)

    if form.is_valid():
        form.save()
        return redirect('/auth/login/')

    context = {
        'form': form,
    }
    return render(request, template, context=context)


class ChangeUserForm(forms.ModelForm):
    class Meta:
        model = User_model
        fields = ['first_name', 'last_name', 'email']


class ChangeProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['birthday']


@login_required
def profile(request):
    template = USER_PROFILE_TEMPLATE

    user = get_user(request)
    user_profile = Profile.objects.filter(user__id=user.id).select_related(
        'user').only('user__id', 'birthday').first()

    items = Rating.objects.filter(user__id=user.id, star=5).select_related(
        'item').select_related('user').only('user__id', 'star', 'item__name')

    profile_form = ChangeProfileForm(request.POST or None,
                                     instance=user_profile)
    user_form = ChangeUserForm(request.POST or None, instance=user)

    if user_form.is_valid() and profile_form.is_valid():
        profile_form.save()
        user_form.save()
    context = {
        'items': items,
        'user_form': user_form,
        'profile_form': profile_form,
    }
    return render(request, template, context=context)
