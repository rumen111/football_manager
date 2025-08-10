from django.contrib import admin
from .models import Match

@admin.register(Match)
class MatchAdmin(admin.ModelAdmin):
    list_display = ('home_team', 'away_team', 'match_date', 'score')
    list_filter = ('match_date', 'home_team', 'away_team')
    search_fields = ('home_team__name', 'away_team__name', 'score')
    ordering = ('-match_date',)
    date_hierarchy = 'match_date'