# Generated by Django 5.1.7 on 2025-03-17 17:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tradingbotweb', '0004_create_currency_model'),
    ]

    operations = [
        migrations.AddField(
            model_name='currencybalance',
            name='value',
            field=models.DecimalField(decimal_places=2, default=0, max_digits=10),
        ),
    ]
