# Generated by Django 3.1.7 on 2021-04-29 06:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('xplorers', '0005_threequarter'),
    ]

    operations = [
        migrations.AlterField(
            model_name='threequarter',
            name='image',
            field=models.ImageField(null=True, upload_to='adverts_three_quarter/%Y/%m/%d'),
        ),
    ]