# Generated by Django 3.1.7 on 2021-06-01 15:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0003_userorder_delivery_type'),
    ]

    operations = [
        migrations.AddField(
            model_name='visitororder',
            name='delivery_Type',
            field=models.CharField(choices=[('Normal (Single)', 'Normal (Single)'), ('Joined (To be delivered with orders in the same area)', 'Joined (To be delivered with orders in the same area)')], default='Normal (Single)', max_length=53, null=True),
        ),
    ]
