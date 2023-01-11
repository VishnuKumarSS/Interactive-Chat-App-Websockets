import datetime
from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
from django.template.defaultfilters import slugify 


class Messages(models.Model):
    user = models.ForeignKey(User, on_delete = models.CASCADE) # blank=True # blank = True is used when system need to give some empty string '' to match the other fields... Its's mainly used when system need to give some data.
    message = models.CharField(max_length = 50)
    created_on = models.DateTimeField(auto_now_add=True)
    room = models.ForeignKey(
        'Room', on_delete=models.CASCADE
    )
    image = models.ForeignKey(
        "ImageUpload", on_delete=models.CASCADE, blank=True, null=True
    )

    class Meta:
        ordering = ['-created_on']

    def __str__(self):
        return f"{self.user} | {self.room} | {self.image} | {self.message}"


class Room(models.Model):
    name = models.CharField(max_length=250, blank=True)
    room_slug = models.SlugField(null=True, unique=True)

    def __str__(self):
        return f"{self.name}"

    def save(self, *args, **kwargs):
        # to create a slug field to use in URL's
        if not self.room_slug:
            self.room_slug = slugify(self.name)
        return super().save(*args, **kwargs)


class ImageUpload(models.Model):
    # user = models.ForeignKey(User, on_delete = models.CASCADE)
    # room = models.ForeignKey('Room', on_delete=models.CASCADE, blank=True)
    title = models.CharField(max_length=200, blank=True)
    image = models.ImageField(upload_to='images')

    def __str__(self):
        return f"Image - {self.title}"
