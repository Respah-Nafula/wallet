# Generated by Django 4.0.6 on 2022-08-10 18:39

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('walletapp', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='reward',
            old_name='points',
            new_name='loyalty_points',
        ),
        migrations.RemoveField(
            model_name='wallet',
            name='currency',
        ),
    ]