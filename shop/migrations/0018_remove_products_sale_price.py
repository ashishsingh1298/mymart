# Generated by Django 3.0.5 on 2020-09-19 07:02

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0017_orders_special'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='products',
            name='sale_price',
        ),
    ]