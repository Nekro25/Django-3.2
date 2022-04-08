from random import sample

from django.shortcuts import render

from catalog.models import Item


def home(request):
    template = 'homepage/home.html'
    all_items = Item.objects.all().filter(is_published=True).prefetch_related(
        'tags')
    if len(all_items) > 3:
        items = sample(list(all_items), k=3)
    else:
        items = all_items

    # Я так сделал из-за того, что не смог найти аналог split для шаблона
    context = {
        'items': [{'name': i.name, 'text': ' '.join(i.text.split()[:10]),
                   'tags': i.tags.all} for i in items],
    }
    return render(request, template, context)
