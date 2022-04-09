from random import sample

from django.shortcuts import render

from catalog.models import Item
from constants import HOMEPAGE_ITEMS_COUNT, HOMEPAGE_HOME_TEMPLATE


def home(request):
    template = HOMEPAGE_HOME_TEMPLATE
    all_items = Item.objects.item_and_tags_is_published().only('name', 'text')
    if len(all_items) > HOMEPAGE_ITEMS_COUNT:
        items = sample(list(all_items), k=HOMEPAGE_ITEMS_COUNT)
    else:
        items = all_items

    context = {
        'items': items,
    }
    return render(request, template, context)
