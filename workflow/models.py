from django.contrib.auth.models import AbstractUser, User
from django.db import models


class UserProfile (models.Model):
    ROLE_CHOICES = (
        ('student', 'student'),
        ('professor', 'professor'),
        ('admin', 'admin'),
    )

    user = models.OneToOneField (User, blank=True, null=True, on_delete=models.CASCADE, related_name='profile')
    role = models.CharField (max_length=20, choices=ROLE_CHOICES, default='student')

    def __str__(self):
        return f'{self.user}_{self.role}'

def get_role(user):
    if hasattr (user, 'profile'):
        return user.profile.role
    return ''

