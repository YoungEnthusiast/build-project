# Generated by Django 3.1.7 on 2021-04-02 05:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0008_auto_20210402_0619'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userorder',
            name='order_Id',
            field=models.CharField(default='BQ35473218', editable=False, max_length=12, null=True),
        ),
        migrations.AlterField(
            model_name='visitororder',
            name='order_Id',
            field=models.CharField(default=33855568, editable=False, max_length=12, null=True),
        ),
    ]
