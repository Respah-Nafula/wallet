# Generated by Django 4.1.1 on 2022-09-07 15:47

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('walletapp', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='receipt',
            name='transaction',
        ),
    ]
