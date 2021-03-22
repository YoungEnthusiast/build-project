from django.db import models
from django.conf import settings
from django.contrib.auth.models import User

class Customer(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    address = models.CharField(max_length=200, null=True)
    city = models.CharField(max_length=20, null=True)
    state = models.CharField(max_length=20, null=True)
    wallet = models.DecimalField(max_digits=11, decimal_places=2, null=True)

    def __str__(self):
        return str(self.user.username)
        #return 'Profile for user {}'.format(self.user.username)

    def get_absolute_url(self):
        return reverse('detail', kwargs={'pk': self.pk})
