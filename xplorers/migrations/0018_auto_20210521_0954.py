# Generated by Django 3.1.7 on 2021-05-21 08:54

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('xplorers', '0017_auto_20210515_1338'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='subscription',
            options={'ordering': ('-date_Activated',)},
        ),
    ]
