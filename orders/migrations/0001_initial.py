# Generated by Django 3.1.7 on 2021-05-30 09:38

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('products', '0028_auto_20210428_2352'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='UserOrder',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('order_Id', models.CharField(default=2021, max_length=10, null=True)),
                ('payment_Mode', models.CharField(choices=[('Pay Instantly', 'Pay Instantly'), ('Pay on Site', 'Pay on Site')], default='Pay Instantly', max_length=14, null=True)),
                ('schedule_Delivery', models.DateField(blank=True, null=True)),
                ('email', models.EmailField(max_length=254, null=True)),
                ('phone_Number', models.CharField(max_length=20, null=True)),
                ('state', models.CharField(choices=[('Select a State', 'Select a State'), ('Ekiti', 'Ekiti'), ('Kwara', 'Kwara'), ('Lagos', 'Lagos'), ('Ogun', 'Ogun'), ('Ondo', 'Ondo'), ('Osun', 'Osun'), ('Oyo', 'Oyo')], default='Select a State', max_length=14, null=True)),
                ('city', models.CharField(blank=True, max_length=20, null=True)),
                ('address', models.CharField(blank=True, max_length=255, null=True)),
                ('date_Ordered', models.DateTimeField(auto_now_add=True)),
                ('last_Modified', models.DateTimeField(auto_now=True)),
                ('order_Status', models.CharField(choices=[('Delivered', 'Delivered'), ('New', 'New'), ('Out for Delivery', 'Out for Delivery')], default='New', max_length=16, null=True)),
                ('delivery_Status', models.CharField(default='New', max_length=3, null=True)),
                ('payment_Status', models.CharField(choices=[('Unconfirmed', 'Unconfirmed'), ('Confirmed', 'Confirmed')], default='Unconfirmed', max_length=12, null=True)),
                ('user', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'ordering': ('-date_Ordered',),
            },
        ),
        migrations.CreateModel(
            name='VisitorOrder',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('order_Id', models.CharField(default=2021, editable=False, max_length=10, null=True)),
                ('first_Name', models.CharField(max_length=30, null=True)),
                ('last_Name', models.CharField(max_length=30, null=True)),
                ('payment_Mode', models.CharField(choices=[('Pay Instantly', 'Pay Instantly'), ('Pay on Site', 'Pay on Site')], default='Pay Instantly', max_length=14, null=True)),
                ('schedule_Delivery', models.DateField(blank=True, null=True)),
                ('email', models.EmailField(max_length=254, null=True)),
                ('phone_Number', models.CharField(max_length=20, null=True)),
                ('state', models.CharField(choices=[('Select a State', 'Select a State'), ('Ekiti', 'Ekiti'), ('Kwara', 'Kwara'), ('Lagos', 'Lagos'), ('Ogun', 'Ogun'), ('Ondo', 'Ondo'), ('Osun', 'Osun'), ('Oyo', 'Oyo')], default='Select a State', max_length=14, null=True)),
                ('city', models.CharField(blank=True, max_length=20, null=True)),
                ('address', models.CharField(blank=True, max_length=255, null=True)),
                ('date_Ordered', models.DateTimeField(auto_now_add=True)),
                ('last_Modified', models.DateTimeField(auto_now=True)),
                ('order_Status', models.CharField(choices=[('Delivered', 'Delivered'), ('New', 'New'), ('Out for Delivery', 'Out for Delivery')], default='New', max_length=16, null=True)),
                ('delivery_Status', models.CharField(default='New', max_length=3, null=True)),
                ('payment_Status', models.CharField(choices=[('Unconfirmed', 'Unconfirmed'), ('Confirmed', 'Confirmed')], default='Unconfirmed', max_length=12, null=True)),
            ],
            options={
                'ordering': ('-date_Ordered',),
            },
        ),
        migrations.CreateModel(
            name='VisitorOrderItem',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('price', models.DecimalField(decimal_places=2, max_digits=10)),
                ('quantity', models.PositiveIntegerField(default=1)),
                ('order', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='visitor_items', to='orders.visitororder')),
                ('product', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='visitor_order_items', to='products.product')),
            ],
        ),
        migrations.CreateModel(
            name='UserOrderStatus',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
                ('order', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='order_status_items', to='orders.userorder')),
            ],
            options={
                'verbose_name': 'User Order Status',
                'verbose_name_plural': 'User Order Statuses',
                'ordering': ('-created',),
            },
        ),
        migrations.CreateModel(
            name='OrderItem',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('price', models.DecimalField(decimal_places=2, max_digits=10)),
                ('quantity', models.PositiveIntegerField(default=1)),
                ('order', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='items', to='orders.userorder')),
                ('product', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='order_items', to='products.product')),
            ],
        ),
    ]
