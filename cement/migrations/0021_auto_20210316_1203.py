# Generated by Django 3.1.7 on 2021-03-16 11:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cement', '0020_auto_20210316_1144'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cementorder',
            name='city',
            field=models.CharField(blank=True, max_length=20, null=True),
        ),
        migrations.AlterField(
            model_name='cementorder',
            name='state',
            field=models.CharField(blank=True, max_length=20, null=True),
        ),
        migrations.AlterField(
            model_name='cementorder',
            name='time',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
    ]