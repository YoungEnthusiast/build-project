# Generated by Django 3.1.7 on 2021-03-22 11:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cement', '0036_auto_20210322_1234'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cementorder',
            name='time',
            field=models.DateTimeField(blank=True, null=True),
        ),
    ]