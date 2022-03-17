from django.urls import path, include
from .views import description

urlpatterns = [
    path('', description),
]
