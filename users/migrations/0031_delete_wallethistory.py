# Generated by Django 3.1.7 on 2021-04-01 16:50

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0030_auto_20210330_1238'),
    ]

    operations = [
        migrations.DeleteModel(
            name='WalletHistory',
        ),
    ]
