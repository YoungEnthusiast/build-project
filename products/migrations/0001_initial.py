# Generated by Django 3.1.7 on 2021-04-02 09:29

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('type', models.CharField(max_length=200, unique=True)),
                ('price', models.DecimalField(decimal_places=2, max_digits=11)),
                ('date', models.DateField(null=True)),
                ('image', models.ImageField(null=True, upload_to='products_img/%Y/%m/%d')),
            ],
            options={
                'ordering': ('type',),
            },
        ),
        migrations.CreateModel(
            name='RegisteredOrder',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('order_Id', models.CharField(default='BQ66359411', editable=False, max_length=10, null=True, unique=True)),
                ('quantity', models.IntegerField(default=1)),
                ('payment_Mode', models.CharField(choices=[('Pay Instantly', 'Pay Instantly'), ('Pay on Site', 'Pay on Site')], default='Pay Instantly', max_length=14, null=True)),
                ('schedule_Delivery', models.DateField(blank=True, null=True)),
                ('email', models.EmailField(max_length=254, null=True)),
                ('phone_Number', models.CharField(max_length=20, null=True)),
                ('state', models.CharField(choices=[('Abia', 'Abia'), ('Adamawa', 'Adamawa'), ('Akwa Ibom', 'Akwa Ibom'), ('Anambra', 'Anambra'), ('Bauchi', 'Bauchi'), ('Bayelsa', 'Bayelsa'), ('Benue', 'Benue'), ('Borno', 'Borno'), ('Cross River', 'Cross River'), ('Delta', 'Delta'), ('Ebonyi', 'Ebonyi'), ('Edo', 'Edo'), ('Ekiti', 'Ekiti'), ('Enugu', 'Enugu'), ('FCT', 'FCT'), ('Gombe', 'Gombe'), ('Imo', 'Imo'), ('Jigawa', 'Jigawa'), ('Kaduna', 'Kaduna'), ('Kano', 'Kano'), ('Katsina', 'Katsina'), ('Kebbi', 'Kebbi'), ('Kogi', 'Kogi'), ('Kwara', 'Kwara'), ('Lagos', 'Lagos'), ('Nasarawa', 'Nasarawa'), ('Niger', 'Niger'), ('Ogun', 'Ogun'), ('Ondo', 'Ondo'), ('Osun', 'Osun'), ('Oyo', 'Oyo'), ('Plateau', 'Plateau'), ('Rivers', 'Rivers'), ('Sokoto', 'Sokoto'), ('Taraba', 'Taraba'), ('Yobe', 'Yobe'), ('Zamfara', 'Zamfara')], default='Abia', max_length=11, null=True)),
                ('city', models.CharField(blank=True, max_length=20, null=True)),
                ('address', models.CharField(blank=True, max_length=255, null=True)),
                ('date_Ordered', models.DateTimeField(auto_now_add=True)),
                ('last_Modified', models.DateTimeField(auto_now=True)),
                ('order_Status', models.CharField(choices=[('Completed', 'Completed'), ('New', 'New'), ('Pending', 'Pending')], default='New', max_length=9, null=True)),
                ('payment_Status', models.CharField(choices=[('Unconfirmed', 'Unconfirmed'), ('Confirmed', 'Confirmed')], default='Unconfirmed', max_length=12, null=True)),
                ('checked', models.BooleanField(default='False')),
                ('product', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='products.product')),
                ('user', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'ordering': ('-date_Ordered',),
            },
        ),
        migrations.CreateModel(
            name='ProductCredit',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('amount_Paid', models.DecimalField(decimal_places=2, max_digits=15, null=True)),
                ('transaction_Date', models.DateField()),
                ('transaction_Name', models.CharField(max_length=45, null=True)),
                ('payment_Evidence', models.ImageField(null=True, upload_to='payment/%Y/%m/%d')),
                ('date_Submitted', models.DateTimeField(auto_now_add=True)),
                ('user', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'ordering': ('-date_Submitted',),
            },
        ),
        migrations.CreateModel(
            name='GuestOrder',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('order_Id', models.CharField(default='BQ10993201', editable=False, max_length=10, null=True, unique=True)),
                ('name', models.CharField(max_length=200)),
                ('email', models.EmailField(max_length=254, null=True)),
                ('phone_Number', models.CharField(max_length=20, null=True)),
                ('state', models.CharField(choices=[('Abia', 'Abia'), ('Adamawa', 'Adamawa'), ('Akwa Ibom', 'Akwa Ibom'), ('Anambra', 'Anambra'), ('Bauchi', 'Bauchi'), ('Bayelsa', 'Bayelsa'), ('Benue', 'Benue'), ('Borno', 'Borno'), ('Cross River', 'Cross River'), ('Delta', 'Delta'), ('Ebonyi', 'Ebonyi'), ('Edo', 'Edo'), ('Ekiti', 'Ekiti'), ('Enugu', 'Enugu'), ('FCT', 'FCT'), ('Gombe', 'Gombe'), ('Imo', 'Imo'), ('Jigawa', 'Jigawa'), ('Kaduna', 'Kaduna'), ('Kano', 'Kano'), ('Katsina', 'Katsina'), ('Kebbi', 'Kebbi'), ('Kogi', 'Kogi'), ('Kwara', 'Kwara'), ('Lagos', 'Lagos'), ('Nasarawa', 'Nasarawa'), ('Niger', 'Niger'), ('Ogun', 'Ogun'), ('Ondo', 'Ondo'), ('Osun', 'Osun'), ('Oyo', 'Oyo'), ('Plateau', 'Plateau'), ('Rivers', 'Rivers'), ('Sokoto', 'Sokoto'), ('Taraba', 'Taraba'), ('Yobe', 'Yobe'), ('Zamfara', 'Zamfara')], default='Abia', max_length=11, null=True)),
                ('city', models.CharField(blank=True, max_length=20, null=True)),
                ('address', models.CharField(blank=True, max_length=255, null=True)),
                ('quantity', models.IntegerField(default=1)),
                ('payment_Mode', models.CharField(choices=[('Pay Instantly', 'Pay Instantly'), ('Pay on Site', 'Pay on Site')], default='Pay Instantly', max_length=14, null=True)),
                ('schedule_Delivery', models.DateField(blank=True, null=True)),
                ('date_Ordered', models.DateTimeField(auto_now_add=True)),
                ('last_Modified', models.DateTimeField(auto_now=True)),
                ('order_Status', models.CharField(choices=[('Completed', 'Completed'), ('New', 'New'), ('Pending', 'Pending')], default='New', max_length=9, null=True)),
                ('payment_Status', models.CharField(choices=[('Unconfirmed', 'Unconfirmed'), ('Confirmed', 'Confirmed')], default='Unconfirmed', max_length=12, null=True)),
                ('product', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='products.product')),
            ],
            options={
                'ordering': ('-date_Ordered',),
            },
        ),
    ]