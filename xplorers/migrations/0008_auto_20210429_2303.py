# Generated by Django 3.1.7 on 2021-04-29 22:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('xplorers', '0007_auto_20210429_0724'),
    ]

    operations = [
        migrations.AddField(
            model_name='full',
            name='expiry',
            field=models.DateField(null=True),
        ),
        migrations.AddField(
            model_name='onequarter',
            name='expiry',
            field=models.DateField(null=True),
        ),
        migrations.AddField(
            model_name='threequarter',
            name='expiry',
            field=models.DateField(null=True),
        ),
    ]
