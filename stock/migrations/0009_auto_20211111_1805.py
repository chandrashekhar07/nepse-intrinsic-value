# Generated by Django 3.2.5 on 2021-11-11 18:05

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('stock', '0008_stockmodel_year'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='stockmodel',
            name='profit',
        ),
        migrations.RemoveField(
            model_name='stockmodel',
            name='shares_outstanding',
        ),
    ]