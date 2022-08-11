# Generated by Django 4.0.6 on 2022-08-10 19:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('walletapp', '0003_remove_card_account'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='customer',
            name='last_name',
        ),
        migrations.AlterField(
            model_name='customer',
            name='gender',
            field=models.CharField(max_length=2),
        ),
        migrations.AlterField(
            model_name='customer',
            name='phone_number',
            field=models.CharField(max_length=10),
        ),
    ]