# Generated by Django 3.1.7 on 2021-03-11 13:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cement', '0027_cementorder_checkout'),
    ]

    operations = [
        migrations.AddField(
            model_name='cementorder',
            name='wallet',
            field=models.DecimalField(decimal_places=2, max_digits=11, null=True),
        ),
    ]
