from django.contrib.auth.models import User
from django.db import models

class Profile(models.Model):
    ROLE_CHOICES = (
        ('manager', 'Manager'),
        ('staff', 'Staff'),
    )

    user = models.OneToOneField(User, on_delete=models.CASCADE)
    bio = models.TextField(blank=True)
    role = models.CharField(max_length=10, choices=ROLE_CHOICES, default='manager')

    def __str__(self):
        return self.user.username