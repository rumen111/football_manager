from django.db import models
from accounts.models import Profile
from django.contrib.auth.models import User

class Tactic(models.Model):
    FORMATION_CHOICES = [
        ("4-4-2", "4-4-2"),
        ("4-3-3", "4-3-3"),
        ("3-5-2", "3-5-2"),
        ("5-3-2", "5-3-2"),
        ("4-2-3-1", "4-2-3-1"),
        ("3-4-3", "3-4-3"),
    ]

    title = models.CharField(max_length=100)
    formation = models.CharField(
        max_length=50,
        choices=FORMATION_CHOICES,
    )
    description = models.TextField()
    created_by = models.ForeignKey(Profile, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.title} ({self.formation})"