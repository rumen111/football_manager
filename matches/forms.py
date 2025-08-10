from django import forms
from .models import Match
from teams.models import Team

class MatchForm(forms.ModelForm):
    class Meta:
        model = Match
        fields = ['home_team', 'away_team', 'match_date', 'score']

    def __init__(self, *args, user=None, **kwargs):
        super().__init__(*args, **kwargs)
        if user is not None:
            my_teams = Team.objects.filter(coach=user)
            self.fields['home_team'].queryset = my_teams
            self.fields['away_team'].queryset = my_teams

    def clean(self):
        cleaned = super().clean()
        home = cleaned.get('home_team')
        away = cleaned.get('away_team')
        if home and away and home == away:
            self.add_error(None, "Home and away team must be different.")
        return cleaned