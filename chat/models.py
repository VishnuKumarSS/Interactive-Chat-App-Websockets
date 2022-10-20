import datetime
from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
from djongo import models as mongo_models

class Messages(models.Model):
    user = models.ForeignKey(User, on_delete = models.CASCADE) # blank=True # blank = True is used when system need to give some empty string '' to match the other fields... Its's mainly used when system need to give some data.
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

class ImageUpload(models.Model):
    user = models.ForeignKey(User, on_delete = models.CASCADE )
    room = models.ForeignKey('Room', on_delete=models.CASCADE)  
    title = models.CharField(max_length=200)
    image = models.ImageField(upload_to='images')

    def __str__(self):
        return f"{self.title}"

# class Log(mongo_models.Model):
#     id = mongo_models.ObjectIdField()
#     message = mongo_models.TextField(max_length=1000)

#     created_at = mongo_models.DateTimeField(auto_now_add=True)
#     updated_at = mongo_models.DateTimeField(auto_now=True)

#     class Meta:
#         _use_db = 'nonrel'
#         ordering = ("-created_at", )

#     def __str__(self):
#         return self.message

# class ImageUploadMongo(mongo_models.Model):
#     id = mongo_models.ObjectIdField()
#     Image = mongo_models.TextField(max_length=1000)
#
#     created_at = mongo_models.DateTimeField(auto_now_add=True)
#     updated_at = mongo_models.DateTimeField(auto_now=True)
#
#     class Meta:
#         _use_db = 'nonrel'
#         ordering = ("-created_at", )
#
#     def __str__(self):
#         return self.id