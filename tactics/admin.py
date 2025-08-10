from django.contrib import admin
from .models import Tactic


@admin.register(Tactic)
class TacticAdmin(admin.ModelAdmin):
    list_display = ('title', 'formation', 'creator_username')
    list_filter = ('formation', 'created_by')
    search_fields = ('title', 'description', 'created_by__user__username')
    ordering = ('title',)
    list_per_page = 25

    def creator_username(self, obj):
        return obj.created_by.user.username

    creator_username.short_description = 'Creator'


