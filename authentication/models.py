from django.db import models
from django.contrib.auth import get_user_model
# Create your models here.

USER=get_user_model()
class Profile(models.Model):
     
    def __str__(self):
        return self.title
    
    