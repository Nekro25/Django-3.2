from django.shortcuts import render, get_object_or_404

from catalog.models import Item
from constants import CATALOG_LIST_TEMPLATE, CATALOG_DETAIL_TEMPLATE


def item_list(request):
    template = CATALOG_LIST_TEMPLATE
    items = Item.objects.item_and_tags_is_published().only('name', 'text')
    context = {
        'items': items,
    }
    return render(request, template, context)


def item_detail(request, item):
    template = CATALOG_DETAIL_TEMPLATE

    product = get_object_or_404(
        Item.objects.item_category_tags_is_published().only('name', 'text',
                                                            'category__name'),
        pk=item)
    context = {
        'item': product
    }
    return render(request, template, context)
