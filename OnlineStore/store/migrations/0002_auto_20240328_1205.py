# Generated by Django 3.2.10 on 2024-03-28 07:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='item',
            name='old_price',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=15, null=True, verbose_name='Старая цена'),
        ),
        migrations.AlterField(
            model_name='item',
            name='price',
            field=models.DecimalField(decimal_places=2, max_digits=15, verbose_name='Новая цена'),
        ),
    ]
