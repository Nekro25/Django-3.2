from django.shortcuts import get_object_or_404, render

from catalog.models import Item


def item_list(request):
    template = 'catalog/list.html'
    items = Item.objects.all().filter(is_published=True).prefetch_related(
        'tags')

    # Я так сделал из-за того, что не смог найти аналог split для шаблона
    context = {
        'items': [{'name': i.name, 'text': ' '.join(i.text.split()[:10]),
                   'tags': i.tags.all} for i in items],
    }
    return render(request, template, context)


def item_detail(request, item):
    template = 'catalog/detail.html'
    product = get_object_or_404(
        Item.objects.select_related('category').prefetch_related('tags'),
        pk=item)
    context = {
        'item': product
    }
    return render(request, template, context)
