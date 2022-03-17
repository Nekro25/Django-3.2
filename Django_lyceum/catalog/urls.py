from django.urls import path, re_path
from .views import item_list, item_detail

urlpatterns = [
    path('', item_list),
    re_path(r'^(?P<item>[\d]+)/$', item_detail),
]


