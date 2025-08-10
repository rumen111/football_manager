from django.core.exceptions import ValidationError
from django.db import models
from django.contrib.auth.models import User



class Team(models.Model):
    name = models.CharField(max_length=100)
    coach = models.ForeignKey(User, on_delete=models.CASCADE, related_name='teams')
    city = models.CharField(max_length=100)
    founded_year = models.IntegerField()
    logo = models.ImageField(upload_to='team_logos/', blank=True, null=True)

    def clean(self):
        # Prevent case-insensitive duplicates
        if Team.objects.filter(name__iexact=self.name).exclude(pk=self.pk).exists():
            raise ValidationError({'name': 'A team with this name already exists.'})

    def __str__(self):
        return self.name

