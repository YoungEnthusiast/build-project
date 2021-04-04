# Generated by Django 3.1.7 on 2021-04-03 16:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0016_auto_20210403_1506'),
    ]

    operations = [
        migrations.RenameField(
            model_name='userorder',
            old_name='checked',
            new_name='checkout_checked',
        ),
        migrations.AddField(
            model_name='userorder',
            name='invoice_checked',
            field=models.BooleanField(default='False'),
        ),
    ]
