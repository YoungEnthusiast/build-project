# Generated by Django 3.1.7 on 2021-04-02 11:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0006_auto_20210402_1155'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userorder',
            name='order_Id',
            field=models.CharField(default='BQ6705998630', editable=False, max_length=12, null=True),
        ),
        migrations.AlterField(
            model_name='visitororder',
            name='order_Id',
            field=models.CharField(default='BQ7690581348', editable=False, max_length=12, null=True),
        ),
    ]
