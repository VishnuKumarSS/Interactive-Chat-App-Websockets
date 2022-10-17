from django.db import models

import datetime
from django.contrib.auth.models import User
from django.utils import timezone
# from django.contrib.auth import get_user_model
# User=get_user_model()


class Messages(models.Model):
    # username = models.CharField(max_length = 40, default="anonymous")
    user = models.ForeignKey(User, on_delete = models.CASCADE) # blank=True # blank = True is used when system need to give some empty string '' to match the other fields... Its's mainly used when system need to give some data.
    # sender = models.ForeignKey(User, on_delete = models.CASCADE, null=True) # blank=True
    # receiver = models.ForeignKey(User, on_delete= models.CASCADE, blank=True)
    message = models.CharField(max_length = 50)
    created_on = models.DateTimeField(auto_now_add=True)
    room = models.ForeignKey('Room', on_delete=models.CASCADE)  
    # created_on = models.DateTimeField(default=timezone.localtime)
    # created_on4 = models.DateTimeField(default=timezone.now)

    class Meta:
        ordering = ['-created_on']

    def __str__(self):
        return f"{self.user} | {self.message}" 
    
class Room(models.Model):
    name = models.CharField(max_length=250, blank=True)
    
    def __str__(self):
        return f"{self.name}" 

