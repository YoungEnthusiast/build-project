from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse

class Category(models.Model):
    type = models.CharField(max_length=200, db_index=True)
    slug = models.SlugField(max_length=200, db_index=True, unique=True)

    class Meta:
        ordering = ('type',)
        verbose_name = 'category'
        verbose_name_plural = 'categories'

    def __str__(self):
        return str(self.type)

    def get_absolute_url(self):
        return reverse('products:product_list_by_category', args=[self.slug])

class Product(models.Model):
	type = models.CharField(max_length=200, db_index=True, unique=True)
	price = models.DecimalField(max_digits=11, decimal_places=2)
	date = models.DateField(null=True)
	image = models.ImageField(upload_to='products_img/%Y/%m/%d', null=True, blank=True)
	category = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True, related_name='products')
	slug = models.SlugField(max_length=200, db_index=True, null=True)
	description = models.TextField(blank=True)
	created = models.DateTimeField(auto_now_add=True, null=True)
	updated = models.DateTimeField(auto_now=True)

	class Meta:
		ordering = ('type',)
		index_together = (('id', 'slug'),)
	def __str__(self):
		return str(self.type)
	@property
	def imageURL(self):
		try:
			url = self.image.url
		except:
			url = ''
		return url

	def get_absolute_url(self):
		return reverse('products:product_detail', args=[self.id, self.slug])

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
