from django.db import models
from django.contrib.auth import get_user_model

USER = get_user_model()

class Profile(models.Model):
    user = models.OneToOneField(USER, on_delete=models.CASCADE, related_name="profile")
    dob = models.DateField(null=True, blank=True)
    profile_pic = models.ImageField(upload_to='profile_pics/', null=True, blank=True)
    position = models.CharField(max_length=100, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title or f"{self.user.username}'s Profile"
