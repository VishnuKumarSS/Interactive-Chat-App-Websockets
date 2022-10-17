from django.contrib import admin

# Register your models here.
from .models import Messages, Room

admin.site.register(Messages)
admin.site.register(Room)