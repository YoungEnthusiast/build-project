# Generated by Django 3.1.7 on 2021-04-02 09:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0003_auto_20210402_1031'),
    ]

    operations = [
        migrations.AlterField(
            model_name='guestorder',
            name='order_Id',
            field=models.CharField(default='BQ29996458', editable=False, max_length=10, null=True, unique=True),
        ),
        migrations.AlterField(
            model_name='registeredorder',
            name='order_Id',
            field=models.CharField(default='BQ29879064', editable=False, max_length=10, null=True, unique=True),
        ),
    ]
