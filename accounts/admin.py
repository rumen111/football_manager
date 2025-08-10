from django.contrib import admin
from .models import Profile

@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    list_display = ('user', 'role', 'bio')            # columns in the list page
    list_filter = ('role',)                           # filter sidebar
    search_fields = ('user__username', 'role', 'bio') # search bar
    ordering = ('user',)                              # default ordering

