from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse

class Product(models.Model):
	type = models.CharField(max_length=200, unique=True)
	price = models.DecimalField(max_digits=11, decimal_places=2)
	date = models.DateField(null=True)
	image = models.ImageField(upload_to='products_img/%Y/%m/%d', null=True)

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

class UserOrder(models.Model):
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
        ('Unconfirmed', 'Unconfirmed'),
        ('Confirmed', 'Confirmed')
    ]
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
	user = models.ForeignKey(User, null=True, blank=True, on_delete=models.SET_NULL)
	product = models.ForeignKey(Product, on_delete=models.SET_NULL, null=True)
	order_Id = models.CharField(
		 max_length = 10,
		 null=True,
		 editable=False,
		 default=2021
	)
	quantity = models.IntegerField(default=1)
	payment_Mode = models.CharField(max_length=14, choices=PAYMENT_CHOICES, default='Pay Instantly', null=True)
	schedule_Delivery = models.DateField(blank=True, null=True)
	email = models.EmailField(null=True)
	phone_Number = models.CharField(max_length=20, null=True)
	state = models.CharField(max_length=14, choices=STATE_CHOICES, default='Select a State', null=True)
	city = models.CharField(max_length=20, null=True, blank=True)
	address = models.CharField(max_length=255, null=True, blank=True)
	date_Ordered = models.DateTimeField(auto_now_add=True)
	last_Modified = models.DateTimeField(auto_now=True)
	order_Status = models.CharField(max_length=9, choices=STATUS_CHOICES, default='New', null=True)
	payment_Status = models.CharField(max_length=12, choices=PAID_CHOICES, default='Unconfirmed', null=True)
	checkout_checked = models.BooleanField(default='False')
	invoice_checked = models.BooleanField(default='False')

	class Meta:
		ordering = ('-date_Ordered',)
	def __str__(self):
		return str(self.order_Id)

	@property
	def total_Price(self):
		total = self.product.price * self.quantity
		return total

	def get_absolute_url(self):
		return reverse('detail', kwargs={'pk': self.pk})

class ProductCredit(models.Model):
	user = models.ForeignKey(User, null=True, blank=True, on_delete=models.SET_NULL)
	amount_Paid = models.DecimalField(null=True, max_digits=15, decimal_places=2)
	transaction_Date = models.DateField(null=True)
	transaction_Name = models.CharField(max_length=45, null=True)
	payment_Evidence = models.ImageField(upload_to='payment/%Y/%m/%d', null=True)
	date_Submitted = models.DateTimeField(auto_now_add=True)

	class Meta:
		ordering = ('-date_Submitted',)

	def __str__(self):
		return str(self.user)

	def get_absolute_url(self):
		return reverse('detail', kwargs={'pk': self.pk})

class VisitorOrder(models.Model):
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
	product = models.ForeignKey(Product, on_delete=models.SET_NULL, null=True)
	order_Id = models.CharField(
		 max_length = 10,
		 null=True,
		 editable=False,
		 default=2021
	)
	name = models.CharField(max_length=200)
	email = models.EmailField(null=True)
	phone_Number = models.CharField(max_length=20, null=True)
	state = models.CharField(max_length=14, choices=STATE_CHOICES, default='Select a State', null=True)
	city = models.CharField(max_length=20, null=True, blank=True)
	address = models.CharField(max_length=255, null=True, blank=True)
	quantity = models.IntegerField(default=1)
	payment_Mode = models.CharField(max_length=14, choices=PAYMENT_CHOICES, default='Pay Instantly', null=True)
	schedule_Delivery = models.DateField(blank=True, null=True)
	date_Ordered = models.DateTimeField(auto_now_add=True)
	last_Modified = models.DateTimeField(auto_now=True)
	order_Status = models.CharField(max_length=9, choices=STATUS_CHOICES, default='New', null=True)
	payment_Status = models.CharField(max_length=12, choices=PAID_CHOICES, default='Unconfirmed', null=True)

	class Meta:
		ordering = ('-date_Ordered',)
	def __str__(self):
		return str(self.order_Id)

	@property
	def total_Price(self):
		total = self.product.price * self.quantity
		return total
