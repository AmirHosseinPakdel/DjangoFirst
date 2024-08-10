from django.db import models


# Create your models here.


class Post(models.Model):
    title = models.CharField(max_length=64)
    description = models.TextField(max_length=1024)
    author = models.CharField(max_length=64)

    # First time it was created
    created_at = models.DateTimeField(auto_now_add=True)

    # Update when edited
    updated_at = models.DateTimeField(null=True, auto_now=True)
