from django.contrib import admin

# Register your models here.
from .models import Messages

admin.site.register(Messages)