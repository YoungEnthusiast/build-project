from django.db import models
from django.contrib.auth.models import User
from users.models import Customer

class Contact(models.Model):
    STATUS_CHOICES = [
        ('Treated','Treated'),
        ('New', 'New'),
        ('Pending', 'Pending')
    ]
    name = models.CharField(max_length=40, blank=True, null=True)
    #user_name = models.ForeignKey(User, on_delete=models.DO_NOTHING)
    email = models.EmailField(null=True)
    phone_number = models.CharField(max_length=20, blank=True, null=True)
    message = models.TextField(max_length=1000, null=True)
    date_submitted = models.DateTimeField(auto_now_add=True)
    status = models.CharField(max_length=9, choices=STATUS_CHOICES, default='New', null=True)
    user_id = models.IntegerField(blank=True, null=True)

    class Meta:
        ordering = ('-date_submitted',)

    def __str__(self):
        return str(self.name)
