# Generated by Django 3.1.7 on 2021-03-28 23:00

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0023_auto_20210328_2148'),
    ]

    operations = [
        migrations.RenameField(
            model_name='wallethistory',
            old_name='current_balance',
            new_name='current',
        ),
        migrations.RenameField(
            model_name='wallethistory',
            old_name='previous',
            new_name='previous_balance',
        ),
    ]