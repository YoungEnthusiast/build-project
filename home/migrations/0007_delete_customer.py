# Generated by Django 3.1.7 on 2021-03-07 20:10

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0006_remove_customer_user'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Customer',
        ),
    ]
