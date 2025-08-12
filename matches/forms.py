from django import forms
from .models import Match
from teams.models import Team

class MatchForm(forms.ModelForm):
    class Meta:
        model = Match
        fields = ['home_team', 'away_team', 'match_date', 'score']

    def __init__(self, *args, user=None, **kwargs):
        super().__init__(*args, **kwargs)

        # Staff with scheduling rights (or superuser) -> all teams
        if user and (user.has_perm('matches.schedule_match') or user.is_superuser or user.is_staff):
            qs = Team.objects.all()
        else:
            # Fallback: limit to user's own teams (shouldn't normally happen if you gate views)
            qs = Team.objects.filter(coach=user) if user else Team.objects.none()

        self.fields['home_team'].queryset = qs
        self.fields['away_team'].queryset = qs

    def clean(self):
        cleaned = super().clean()
        home = cleaned.get('home_team')
        away = cleaned.get('away_team')
        if home and away and home == away:
            # form-level validation (model has a check constraint too)
            self.add_error('away_team', "Home and away team must be different.")
        return cleaned