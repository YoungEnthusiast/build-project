# Generated by Django 3.1.7 on 2021-03-30 09:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0026_remove_wallethistory_amount_paid'),
    ]

    operations = [
        migrations.AddField(
            model_name='customer',
            name='phone_number',
            field=models.CharField(max_length=20, null=True),
        ),
    ]