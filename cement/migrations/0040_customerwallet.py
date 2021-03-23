# Generated by Django 3.1.7 on 2021-03-23 17:40

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('users', '0009_delete_wallet'),
        ('cement', '0039_auto_20210323_1107'),
    ]

    operations = [
        migrations.CreateModel(
            name='CustomerWallet',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('amount_Paid', models.DecimalField(decimal_places=2, max_digits=11, null=True)),
                ('transaction_Date', models.DateField()),
                ('transaction_Name', models.CharField(max_length=45, null=True)),
                ('payment_Evidence', models.ImageField(null=True, upload_to='')),
                ('date_Submitted', models.DateTimeField(auto_now_add=True)),
                ('wallet_customer', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='users.customer')),
                ('wallet_user', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'ordering': ('-date_Submitted',),
            },
        ),
    ]
