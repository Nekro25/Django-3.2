from django.contrib.auth.views import LoginView, LogoutView, \
    PasswordChangeView, PasswordChangeDoneView, PasswordResetView, \
    PasswordResetCompleteView, PasswordResetConfirmView, PasswordResetDoneView
from django.urls import path, re_path, include

from .views import user_list, user_detail, profile, signup

user = [
    path('', user_list),
    re_path(r'^(?P<item>[\d]+)/$', user_detail),
]

urlpatterns = [
    path(
        'login/',
        LoginView.as_view(template_name='users/login.html'),
        name='login'
    ),
    path(
        'logout/',
        LogoutView.as_view(template_name='users/logout.html'),
        name='logout'
    ),
    path(
        'password_change/',
        PasswordChangeView.as_view(template_name='users/password_change.html'),
        name='password_change'
    ),
    path(
        'password_change/done/',
        PasswordChangeDoneView.as_view(
            template_name='users/password_change_done.html'),
        name='password_change_done'
    ),
    path(
        'password_reset/',
        PasswordResetView.as_view(template_name='users/password_reset.html'),
        name='password_reset'
    ),
    path(
        'password_reset/done/',
        PasswordResetDoneView.as_view(
            template_name='users/password_reset_done.html'),
        name='password_reset_done'
    ),
    path(
        'reset/<uidb64>/<token>/',
        PasswordResetConfirmView.as_view(
            template_name='users/password_reset_confirm.html'),
        name='password_reset_confirm'
    ),
    path(
        'reset/done/',
        PasswordResetCompleteView.as_view(
            template_name='users/password_reset_complete.html'),
        name='password_reset_complete'
    ),
    path('users/', include(user)),
    path('signup/', signup),
    path('profile/', profile),
]
