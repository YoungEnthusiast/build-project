# Generated by Django 3.1.7 on 2021-03-11 14:04

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('cement', '0023_auto_20210311_1502'),
    ]

    operations = [
        migrations.RenameField(
            model_name='cementorder',
            old_name='checkout',
            new_name='acheckout',
        ),
    ]