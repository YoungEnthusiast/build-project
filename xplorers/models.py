from django.db import models
from django.conf import settings
from django.contrib.auth.models import User

class XploreCustomer(models.Model):
    STATE_CHOICES = [
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
    state = models.CharField(max_length=11, choices=STATE_CHOICES, default='Abia', null=True)
    city = models.CharField(max_length=20, null=True)
    address = models.CharField(max_length=200, null=True)
    CAC_Certificate = models.ImageField(upload_to='CAC_Xplore/%Y/%m/%d', null=True)
    last_Modified = models.DateTimeField(auto_now=True)

    def __str__(self):
        return str(self.user.username)
        #return 'Profile for user {}'.format(self.user.username)

    class Meta:
        ordering = ('user',)

    def get_absolute_url(self):
        return reverse('detail', kwargs={'pk': self.pk})

class Request(models.Model):
    PACKAGE_CHOICES = [
		('One Quarter: ₦---', 'One Quarter: ₦---'),
		('Three Quarters: ₦---', 'Three Quarters: ₦---'),
		('Full Width: ₦---', 'Full Width: ₦---'),
        ('Home Page: ₦---', 'Home Page: ₦---'),
        ]
    user = models.ForeignKey(User, null=True, blank=True, on_delete=models.SET_NULL)
    package = models.CharField(max_length=20, choices=PACKAGE_CHOICES, default='One Quarter: ₦---', null=True)
    image = models.ImageField(upload_to='advert_image/%Y/%m/%d', null=True)
    payment_Evidence = models.ImageField(upload_to='payment_xplorer/%Y/%m/%d', null=True)
    waiver_Code = models.CharField(max_length=10, null=True)
    created = models.DateTimeField(auto_now_add=True, null=True)

    def __str__(self):
        return str(self.id)

    class Meta:
        ordering = ('-created',)

    @property
    def imageURL(self):
        try:
            url = self.image.url
        except:
            url = ''
        return url

class Subscription(models.Model):
    PACKAGE_CHOICES = [
		('One Quarter', 'One Quarter'),
		('Three Quarters', 'Three Quarters'),
		('Full Width', 'Full Width'),
        ('Home Page', 'Home Page'),
        ]
    xplorer = models.ForeignKey(XploreCustomer, on_delete=models.SET_NULL, null=True)
    request_Id = models.ForeignKey(Request, on_delete=models.SET_NULL, null=True)
    package = models.CharField(max_length=14, choices=PACKAGE_CHOICES, default='One Quarter', null=True)
    date_Activated = models.DateTimeField(auto_now_add=True, null=True)
    subscription_Ends = models.DateField(null=True)

    def __str__(self):
        return str(self.request_Id)

    class Meta:
        ordering = ('-date_Activated',)
