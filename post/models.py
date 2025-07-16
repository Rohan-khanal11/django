from django.db import models
from django.contrib.auth import get_user_model
# Create your models here.

USER=get_user_model()
class Post(models.Model):
    title = models.CharField(max_length=120,null=False,blank=False )
    body=models.TextField(blank=False,null=False)
    author=models.ForeignKey(USER, blank=False,null=False, on_delete=models.DO_NOTHING)
    
    def __str__(self):
        return self.title
    
    