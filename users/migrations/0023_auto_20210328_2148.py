# Generated by Django 3.1.7 on 2021-03-28 20:48

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0022_auto_20210328_2134'),
    ]

    operations = [
        migrations.RenameField(
            model_name='wallethistory',
            old_name='previous_balance',
            new_name='previous',
        ),
    ]
