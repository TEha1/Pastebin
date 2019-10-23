
from django.contrib.auth.models import User
from django.db import models

# Create your models here.

class Pastebin(models.Model):
    PRIVATE = 1
    USERS = 2
    PUBLIC = 3
    PRIVACY_CHOICES = [
        (PRIVATE, "private"),
        (USERS, "certain users"),
        (PUBLIC, "public"),
    ]
    paste_text = models.TextField()
    date = models.DateField(auto_now_add=True, blank=True)
    privacy = models.PositiveSmallIntegerField(choices=PRIVACY_CHOICES, default=PUBLIC)
    user = models.ForeignKey(to=User, on_delete=models.CASCADE, null=True, blank=True)

    def __str__(self):
        return self.paste_text