from django.db import models
from django.contrib.auth.models import User

class Contact(models.Model):
    STATUS_CHOICES = [
        ('Treated','Treated'),
        ('New', 'New'),
        ('Pending', 'Pending')
    ]
    name = models.CharField(max_length=40, blank=True, null=True)
    email = models.EmailField(null=True)
    phone_Number = models.CharField(max_length=20, blank=True, null=True)
    message = models.TextField(max_length=1000, null=True)
    date_Submitted = models.DateTimeField(auto_now_add=True)
    status = models.CharField(max_length=9, choices=STATUS_CHOICES, default='New', null=True)

    class Meta:
        ordering = ('-date_Submitted',)

    def __str__(self):
        return str(self.name)
