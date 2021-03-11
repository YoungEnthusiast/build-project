from django.db import models
from django.conf import settings
from django.contrib.auth.models import User

class Customer(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    address = models.CharField(max_length=200)
    city = models.CharField(max_length=20)
    state = models.CharField(max_length=20)

    def __str__(self):
        return 'Profile for user {}'.format(self.user.username)
