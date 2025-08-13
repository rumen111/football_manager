from django.core.validators import MinValueValidator
from django.db import models
from django.contrib.auth.models import User

from teams.models import Team


class Player(models.Model):
    POSITION_CHOICES = [
        ('GK', 'Goalkeeper'),
        ('DF', 'Defender'),
        ('MF', 'Midfielder'),
        ('FW', 'Forward'),
    ]

    name = models.CharField(max_length=100)
    team = models.ForeignKey(Team, on_delete=models.CASCADE, related_name='players')
    age = models.PositiveSmallIntegerField(
        validators=[MinValueValidator(12, message="Minimum age is 12.")]
    )
    position = models.CharField(max_length=2, choices=POSITION_CHOICES)
    nationality = models.CharField(max_length=100, default='Unknown')

    def __str__(self):
        return f"{self.name} ({self.get_position_display()})"