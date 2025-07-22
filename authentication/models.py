from django.db import models
from django.contrib.auth import get_user_model

USER = get_user_model()

POSITION_CHOICE = [
    ("fr", "First Position"),
    ("sc", "Second Position"),
    ("tr", "Third Position"),
    ("fu", "Fourth Position"),
    ("fi", "Fifth Position"),
]

class Profile(models.Model):
    user = models.OneToOneField(USER, on_delete=models.CASCADE)
    dob = models.DateField()
    position = models.CharField(max_length=2, choices=POSITION_CHOICE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.user.username}'s Profile"
