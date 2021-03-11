from django.db import models
from django.contrib.auth.models import User

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
	STATUS_CHOICES = [
        ('Completed','Completed'),
        ('New', 'New'),
        ('Pending', 'Pending')
    ]
	user = models.ForeignKey(User, null=True, blank=True, on_delete=models.CASCADE)
	cement = models.ForeignKey(Cement, on_delete=models.SET_NULL, null=True)
	quantity = models.IntegerField(default=0)
	date_ordered = models.DateTimeField(auto_now_add=True)
	last_modified = models.DateTimeField(auto_now=True)
	status = models.CharField(max_length=9, choices=STATUS_CHOICES, default='New', null=True)

	class Meta:
		ordering = ('-id',)
	def __str__(self):
		return str(self.id)

	@property
	def total_price(self):
		total = self.cement.price * self.quantity
		return total

class GuestCementOrder(models.Model):
	STATUS_CHOICES = [
        ('Completed','Completed'),
        ('New', 'New'),
        ('Pending', 'Pending')
    ]
	cement = models.ForeignKey(Cement, on_delete=models.SET_NULL, null=True)
	name = models.CharField(max_length=200)
	address = models.CharField(max_length=200)
	city = models.CharField(max_length=20)
	state = models.CharField(max_length=20)
	quantity = models.IntegerField(default=0)
	date_ordered = models.DateTimeField(auto_now_add=True)
	status = models.CharField(max_length=9, choices=STATUS_CHOICES, default='New', null=True)

	class Meta:
		ordering = ('-id',)
	def __str__(self):
		return str(self.id)

	@property
	def total_price(self):
		total = self.cement.price * self.quantity
		return total
	
