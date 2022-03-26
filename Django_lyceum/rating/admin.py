from django.contrib import admin

from rating.models import Rating


@admin.register(Rating)
class RatingAdmin(admin.ModelAdmin):
    pass
