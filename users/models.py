from django.db import models
from django.conf import settings
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver

class ProductCustomer(models.Model):
    STATE_CHOICES = [
        ('Select a State', 'Select a State'),
		('Abia', 'Abia'),
		('Adamawa', 'Adamawa'),
		('Akwa Ibom', 'Akwa Ibom'),
		('Anambra', 'Anambra'),
		('Bauchi', 'Bauchi'),
		('Bayelsa', 'Bayelsa'),
		('Benue', 'Benue'),
		('Borno', 'Borno'),
		('Cross River', 'Cross River'),
		('Delta', 'Delta'),
		('Ebonyi', 'Ebonyi'),
		('Edo', 'Edo'),
		('Ekiti', 'Ekiti'),
		('Enugu', 'Enugu'),
		('FCT', 'FCT'),
		('Gombe', 'Gombe'),
		('Imo', 'Imo'),
		('Jigawa', 'Jigawa'),
		('Kaduna', 'Kaduna'),
		('Kano', 'Kano'),
		('Katsina', 'Katsina'),
		('Kebbi', 'Kebbi'),
		('Kogi', 'Kogi'),
		('Kwara', 'Kwara'),
		('Lagos', 'Lagos'),
		('Nasarawa', 'Nasarawa'),
		('Niger', 'Niger'),
		('Ogun', 'Ogun'),
		('Ondo', 'Ondo'),
		('Osun', 'Osun'),
		('Oyo', 'Oyo'),
		('Plateau', 'Plateau'),
		('Rivers', 'Rivers'),
		('Sokoto', 'Sokoto'),
		('Taraba', 'Taraba'),
		('Yobe', 'Yobe'),
		('Zamfara', 'Zamfara')
	]
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    phone_Number = models.CharField(max_length=20, null=True)
    state = models.CharField(max_length=14, choices=STATE_CHOICES, default='Select a State', null=True)
    city = models.CharField(max_length=20, null=True)
    address = models.CharField(max_length=200, null=True)
    CAC_Certificate = models.ImageField(upload_to='CAC_Certs/%Y/%m/%d', null=True, blank=True)
    last_Modified = models.DateTimeField(auto_now=True)
    email_confirmed = models.BooleanField(default=False)

    @receiver(post_save, sender=User)
    def update_user_profile(sender, instance, created, **kwargs):
        if created:
            ProductCustomer.objects.create(user=instance)
            instance.productcustomer.save()

    def __str__(self):
        return str(self.user.username)
        #return 'Profile for user {}'.format(self.user.username)

    class Meta:
        ordering = ('user',)

    def get_absolute_url(self):
        return reverse('detail', kwargs={'pk': self.pk})

class ProductWalletHistorie(models.Model):
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    amount_debited = models.DecimalField(blank=True, null=True, max_digits=15, decimal_places=2)
    last_tran = models.DecimalField(blank=True, null=True, max_digits=15, decimal_places=2)
    amount_credited = models.DecimalField(blank=True, null=True, max_digits=15, decimal_places=2)
    current_balance = models.DecimalField(blank=True, null=True, max_digits=15, decimal_places=2)
    date_recorded = models.DateTimeField(auto_now_add=True, null=True)
    last_modified = models.DateTimeField(auto_now=True)

    def __str__(self):
        return str(self.user.username)

    class Meta:
        ordering = ('-date_recorded',)
