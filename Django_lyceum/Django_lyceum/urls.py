from django.contrib import admin
from django.urls import path, re_path
from homepage.views import home
from catalog.views import item_list, item_detail
from about.views import description
from users.views import user_list, user_detail, signup, profile

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home),
    path('catalog/', item_list),
    re_path('catalog/(?P<item>[\d]+)', item_detail),
    path('about/', description),
    path('auth/users/', user_list),
    re_path('auth/users/(?P<item>[\d]+)', user_detail),
    path('auth/signup/', signup),
    path('auth/profile/', profile),
]
