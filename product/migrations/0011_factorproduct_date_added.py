# Generated by Django 4.0.6 on 2022-07-11 06:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0010_remove_factor_discount_remove_factor_tax_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='factorproduct',
            name='date_added',
            field=models.DateField(auto_now=True),
        ),
    ]
