from django.shortcuts import render

from constants import ABOUT_DESCRIPTION_TEMPLATE


def description(request):
    template = ABOUT_DESCRIPTION_TEMPLATE
    return render(request, template)
