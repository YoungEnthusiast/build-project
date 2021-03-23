from django.db import models
from django.contrib.auth.models import User
from users.models import Customer
from django.urls import reverse

class Cement(models.Model):
	type = models.CharField(max_length=200, unique=True)
	price = models.DecimalField(max_digits=11, decimal_places=2)
	date = models.DateField(null=True)
	#digital = models.BooleanField(default=False,null=True, blank=True)
	image = models.ImageField(null=True, blank=True)

	class Meta:
		ordering = ('type',)
	def __str__(self):
		return self.type
	@property
	def imageURL(self):
		try:
			url = self.image.url
		except:
			url = ''
		return url

class CementOrder(models.Model):
	PAYMENT_CHOICES = [
		('Pay Instantly','Pay Instantly'),
		('Pay on Site', 'Pay on Site')
	]
	STATUS_CHOICES = [
        ('Completed','Completed'),
        ('New', 'New'),
        ('Pending', 'Pending')
    ]
	PAID_CHOICES = [
        ('Unconfirmed','Unconfirmed'),
        ('Confirmed', 'Confirmed')
    ]

	user = models.ForeignKey(User, null=True, blank=True, on_delete=models.SET_NULL)
	#customer = models.ForeignKey(Customer, null=True, blank=True, on_delete=models.SET_NULL)
	cement = models.ForeignKey(Cement, on_delete=models.SET_NULL, null=True)
	quantity = models.IntegerField(default=0)
	payment_mode = models.CharField(max_length=14, choices=PAYMENT_CHOICES, default='Pay Instantly', null=True)
	schedule_delivery = models.DateField(blank=True, null=True)
	address = models.CharField(max_length=255, null=True, blank=True)
	city = models.CharField(max_length=20, null=True, blank=True)
	state = models.CharField(max_length=20, null=True, blank=True)
	date_ordered = models.DateTimeField(auto_now_add=True)
	last_modified = models.DateTimeField(auto_now=True)
	order_status = models.CharField(max_length=9, choices=STATUS_CHOICES, default='New', null=True)
	payment_status = models.CharField(max_length=12, choices=PAID_CHOICES, default='Unconfirmed', null=True)
	checkout = models.BooleanField(default='False')


	class Meta:
		ordering = ('-id',)
	def __str__(self):
		return str(self.id)

	@property
	def total_price(self):
		total = self.cement.price * self.quantity
		return total

	def get_absolute_url(self):
		return reverse('detail', kwargs={'pk': self.pk})

class CustomerWallet(models.Model):
	user = models.ForeignKey(User, null=True, blank=True, on_delete=models.SET_NULL)
	customer = models.ForeignKey(Customer, null=True, blank=True, on_delete=models.SET_NULL)
	amount_Paid = models.DecimalField( null=True, max_digits=11, decimal_places=2)
	transaction_Date = models.DateField()
	transaction_Name = models.CharField(max_length=45, null=True)
	payment_Evidence = models.ImageField(upload_to='payment/%Y/%m/%d', null=True)
	date_Submitted = models.DateTimeField(auto_now_add=True)

	class Meta:
		ordering = ('-date_Submitted',)

	def __str__(self):
		return str(self.user)

	def get_absolute_url(self):
		return reverse('detail', kwargs={'pk': self.pk})

class GuestCementOrder(models.Model):
	PAYMENT_CHOICES = [
		('Pay Instantly','Pay Instantly'),
		('Pay on Site', 'Pay on Site')
	]
	STATUS_CHOICES = [
        ('Completed','Completed'),
        ('New', 'New'),
        ('Pending', 'Pending')
    ]
	PAID_CHOICES = [
        ('Unconfirmed','Unconfirmed'),
        ('Confirmed', 'Confirmed')
    ]
	cement = models.ForeignKey(Cement, on_delete=models.SET_NULL, null=True)
	name = models.CharField(max_length=200)
	email = models.EmailField(null=True)
	address = models.CharField(max_length=255)
	city = models.CharField(max_length=20)
	state = models.CharField(max_length=20)
	quantity = models.IntegerField(default=0)
	payment_mode = models.CharField(max_length=14, choices=PAYMENT_CHOICES, default='Pay Instantly', null=True)
	schedule_delivery = models.DateField(blank=True, null=True)
	date_ordered = models.DateTimeField(auto_now_add=True)
	order_status = models.CharField(max_length=9, choices=STATUS_CHOICES, default='New', null=True)
	payment_status = models.CharField(max_length=12, choices=PAID_CHOICES, default='Unconfirmed', null=True)

	class Meta:
		ordering = ('-id',)
	def __str__(self):
		return str(self.id)

	@property
	def total_price(self):
		total = self.cement.price * self.quantity
		return total
