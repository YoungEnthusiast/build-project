# Generated by Django 3.1.7 on 2021-05-15 12:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('xplorers', '0015_auto_20210514_1538'),
    ]

    operations = [
        migrations.AddField(
            model_name='subscription',
            name='package',
            field=models.CharField(choices=[('One Quarter', 'One Quarter'), ('Three Quarters', 'Three Quarters'), ('Full Width', 'Full Width'), ('Home Page', 'Home Page')], default='One Quarter', max_length=14, null=True),
        ),
    ]
