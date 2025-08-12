from django.core.exceptions import ValidationError
from django.db import models
from teams.models import Team

class Match(models.Model):
    home_team = models.ForeignKey(Team, related_name='home_matches', on_delete=models.CASCADE)
    away_team = models.ForeignKey(Team, related_name='away_matches', on_delete=models.CASCADE)
    match_date = models.DateField()
    score = models.CharField(max_length=20, blank=True)

    class Meta:
        permissions = [
            ("schedule_match", "Can schedule matches"),
        ]

    def clean(self):
        super().clean()
        if self.home_team_id and self.away_team_id and self.home_team_id == self.away_team_id:
            raise ValidationError("Home and away team must be different.")

    def __str__(self):
        return f"{self.home_team} vs {self.away_team} on {self.match_date}"