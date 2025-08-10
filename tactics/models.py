from django.db import models
from accounts.models import Profile
from django.contrib.auth.models import User


class Tactic(models.Model):
    title = models.CharField(max_length=100)
    formation = models.CharField(max_length=50)  # e.g., "4-4-2"
    description = models.TextField()
    created_by = models.ForeignKey(Profile, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.title} ({self.formation})"