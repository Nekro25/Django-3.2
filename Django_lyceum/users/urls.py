from django.urls import path, re_path, include
from .views import user_list, user_detail, profile, signup

user = [
    path('', user_list),
    re_path(r'^(?P<item>[\d]+)/$', user_detail),
]


urlpatterns = [
    path('users/', include(user)),
    path('signup/', signup),
    path('profile/', profile),
]
