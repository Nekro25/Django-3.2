from django import forms
from django.contrib.auth import get_user
from django.core.exceptions import ObjectDoesNotExist
from django.db.models import Avg
from django.shortcuts import render, get_object_or_404, redirect

from catalog.models import Item
from constants import CATALOG_LIST_TEMPLATE, CATALOG_DETAIL_TEMPLATE
from rating.models import Rating


def item_list(request):
    template = CATALOG_LIST_TEMPLATE
    items = Item.objects.item_and_tags_is_published().only('name', 'text')
    context = {
        'items': items,
    }
    return render(request, template, context)


class StarForm(forms.Form):
    CHOICES = [(1, 'Ненависть'), (2, 'Неприязнь'),
               (3, 'Нейтрально'), (4, 'Обожание'), (5, 'Любовь')]
    star = forms.ChoiceField(
        label='Выберите оценку',
        widget=forms.RadioSelect,
        choices=CHOICES,
    )
    star.required = False


def item_detail(request, item):
    template = CATALOG_DETAIL_TEMPLATE

    form = StarForm(request.POST or None)

    product = get_object_or_404(
        Item.objects.item_category_tags_is_published().only('name', 'text',
                                                            'category__name'),
        pk=item)

    rating = Rating.objects.filter(item__id=item).select_related(
        'item').select_related('user').only('star', 'item__id', 'user')
    user = get_user(request)
    avg = 'Нет данных'
    if rating:
        avg = rating.all().aggregate(Avg('star'))['star__avg']
    try:
        rate = rating.get(user=user.id)
    except ObjectDoesNotExist:
        rate = None

    if form.is_valid():
        Rating.objects.update_or_create(
            star=form.cleaned_data['star'],
            defaults={'item': product, 'user': user})
        return redirect(f'/catalog/{item}/')
    context = {
        'item': product,
        'rating': rating,
        'avg_rating': avg,
        'form': form,
        'user_rate': rate,
    }
    return render(request, template, context)
