# Generated by Django 3.1.7 on 2021-05-14 14:38

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('xplorers', '0014_subscription_xplorer'),
    ]

    operations = [
        migrations.RenameField(
            model_name='request',
            old_name='advert_Image',
            new_name='image',
        ),
    ]
