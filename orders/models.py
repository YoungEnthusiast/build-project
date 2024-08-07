from django.db import models
from django.contrib.auth.models import User
from products.models import Product

class UserOrder(models.Model):
    PAYMENT_CHOICES = [
		('Pay Instantly','Pay Instantly'),
		('Pay on Site', 'Pay on Site')
	]
    STATUS_CHOICES = [
        ('Delivered','Delivered'),
        ('New', 'New'),
        ('Out for Delivery', 'Out for Delivery')
    ]
    PAID_CHOICES = [
        ('Unconfirmed', 'Unconfirmed'),
        ('Confirmed', 'Confirmed')
    ]
    STATE_CHOICES = [
		('Select a State', 'Select a State'),
		('Ekiti', 'Ekiti'),
		('Kwara', 'Kwara'),
		('Lagos', 'Lagos'),
		('Ogun', 'Ogun'),
		('Ondo', 'Ondo'),
		('Osun', 'Osun'),
		('Oyo', 'Oyo')
	]
    DELIVERY_CHOICES = [
        ('Normal (Single)', 'Normal (Single)'),
        ('Joined (To be delivered with orders in the same area)', 'Joined (To be delivered with orders in the same area)')
    ]
    user = models.ForeignKey(User, null=True, blank=True, on_delete=models.SET_NULL)
    order_Id = models.CharField(
		 max_length = 10,
		 null=True,
		 editable=True,
		 default=2021
	)
    payment_Mode = models.CharField(max_length=14, choices=PAYMENT_CHOICES, default='Pay Instantly', null=True)
    delivery_Type = models.CharField(max_length=53, choices=DELIVERY_CHOICES, default='Normal (Single)', null=True)
    schedule_Delivery = models.DateField(blank=True, null=True)
    email = models.EmailField(null=True)
    phone_Number = models.CharField(max_length=20, null=True)
    state = models.CharField(max_length=14, choices=STATE_CHOICES, default='Select a State', null=True)
    city = models.CharField(max_length=20, null=True, blank=True)
    address = models.CharField(max_length=255, null=True, blank=True)
    date_Ordered = models.DateTimeField(auto_now_add=True)
    last_Modified = models.DateTimeField(auto_now=True)
    order_Status = models.CharField(max_length=16, choices=STATUS_CHOICES, default='New', null=True)
    delivery_Status = models.CharField(max_length=3, default='New', null=True)
    payment_Status = models.CharField(max_length=12, choices=PAID_CHOICES, default='Unconfirmed', null=True)

    class Meta:
        ordering = ('-date_Ordered',)

    def __str__(self):
        return str(self.order_Id)

    def get_total_cost(self):
        return sum(item.get_cost() for item in self.items.all())

class OrderItem(models.Model):
    order = models.ForeignKey(UserOrder, on_delete=models.SET_NULL, null=True, related_name='items')
    product = models.ForeignKey(Product, on_delete=models.SET_NULL, null=True, related_name='order_items')
    price = models.DecimalField(max_digits=10, decimal_places=2)
    quantity = models.PositiveIntegerField(default=1)

    def __str__(self):
        return '{}'.format(self.id)

    def get_cost(self):
        if self.price == None:
            pass
        else:
            return self.price * self.quantity

class VisitorOrder(models.Model):
    PAYMENT_CHOICES = [
		('Pay Instantly','Pay Instantly'),
		('Pay on Site', 'Pay on Site')
	]
    STATUS_CHOICES = [
        ('Delivered','Delivered'),
        ('New', 'New'),
        ('Out for Delivery', 'Out for Delivery')
    ]
    PAID_CHOICES = [
        ('Unconfirmed', 'Unconfirmed'),
        ('Confirmed', 'Confirmed')
    ]
    STATE_CHOICES = [
		('Select a State', 'Select a State'),
		('Ekiti', 'Ekiti'),
		('Kwara', 'Kwara'),
		('Lagos', 'Lagos'),
		('Ogun', 'Ogun'),
		('Ondo', 'Ondo'),
		('Osun', 'Osun'),
		('Oyo', 'Oyo')
	]
    DELIVERY_CHOICES = [
        ('Normal (Single)', 'Normal (Single)'),
        ('Joined (To be delivered with orders in the same area)', 'Joined (To be delivered with orders in the same area)')
    ]
    order_Id = models.CharField(
		 max_length = 10,
		 null=True,
		 editable=False,
		 default=2021
	)
    first_Name = models.CharField(max_length=30, null=True)
    last_Name = models.CharField(max_length=30, null=True)
    payment_Mode = models.CharField(max_length=14, choices=PAYMENT_CHOICES, default='Pay Instantly', null=True)
    delivery_Type = models.CharField(max_length=53, choices=DELIVERY_CHOICES, default='Normal (Single)', null=True)
    schedule_Delivery = models.DateField(blank=True, null=True)
    email = models.EmailField(null=True)
    phone_Number = models.CharField(max_length=20, null=True)
    state = models.CharField(max_length=14, choices=STATE_CHOICES, default='Select a State', null=True)
    city = models.CharField(max_length=20, null=True, blank=True)
    address = models.CharField(max_length=255, null=True, blank=True)
    date_Ordered = models.DateTimeField(auto_now_add=True)
    last_Modified = models.DateTimeField(auto_now=True)
    order_Status = models.CharField(max_length=16, choices=STATUS_CHOICES, default='New', null=True)
    delivery_Status = models.CharField(max_length=3, default='New', null=True)
    payment_Status = models.CharField(max_length=12, choices=PAID_CHOICES, default='Unconfirmed', null=True)

    class Meta:
        ordering = ('-date_Ordered',)

    def __str__(self):
        return str(self.order_Id)

    def get_total_cost(self):
        return sum(visitor_item.get_cost() for visitor_item in self.visitor_items.all())

class VisitorOrderItem(models.Model):
    order = models.ForeignKey(VisitorOrder, on_delete=models.SET_NULL, null=True, related_name='visitor_items')
    product = models.ForeignKey(Product, on_delete=models.SET_NULL, null=True, related_name='visitor_order_items')
    price = models.DecimalField(max_digits=10, decimal_places=2)
    quantity = models.PositiveIntegerField(default=1)

    def __str__(self):
        return '{}'.format(self.id)

    def get_cost(self):
        if self.price == None:
            pass
        else:
            return self.price * self.quantity

class OrderStatus(models.Model):
    STATUS_CHOICES = [
        ('Delivered','Delivered'),
        ('Out for Delivery', 'Out for Delivery')
    ]
    order = models.ForeignKey(UserOrder, on_delete=models.SET_NULL, null=True, related_name='order_status_items')
    order_Status = models.CharField(max_length=16, choices=STATUS_CHOICES, default='Out for Delivery', null=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ('-created',)
        verbose_name = 'Order Status'
        verbose_name_plural = 'Order Statuses'

    def __str__(self):
        return str(self.order)
