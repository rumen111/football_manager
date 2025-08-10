from django.contrib import admin
from .models import Team

@admin.register(Team)
class TeamAdmin(admin.ModelAdmin):
    list_display = ('name', 'city', 'founded_year', 'coach')
    list_filter = ('city', 'founded_year')
    search_fields = ('name', 'city')
    ordering = ('name',)