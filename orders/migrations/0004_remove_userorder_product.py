# Generated by Django 3.1.7 on 2021-04-21 15:04

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0003_orderitem_userorder'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='userorder',
            name='product',
        ),
    ]
