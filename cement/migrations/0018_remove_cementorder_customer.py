# Generated by Django 3.1.7 on 2021-03-16 07:44

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('cement', '0017_auto_20210316_0843'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='cementorder',
            name='customer',
        ),
    ]
