from django.contrib import admin
from .models import Player


@admin.register(Player)
class PlayerAdmin(admin.ModelAdmin):
    list_display = ('name', 'position', 'team', 'age', 'nationality')
    list_filter = ('position', 'team', 'nationality')
    search_fields = ('name', 'nationality')
    ordering = ('team', 'position', 'name')

