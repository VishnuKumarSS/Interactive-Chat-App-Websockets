from django.db import models

# Create your models here.
class Messages(models.Model):
    username = models.CharField(max_length = 200, default="new")
    message = models.CharField(max_length = 200)
    created_on = models.DateTimeField(auto_now_add=True)

    
    class Meta:
        ordering = ['-created_on']
        
    def __str__(self):
        return f"{self.username} | {self.message} | {self.created_on}" 
    

    

