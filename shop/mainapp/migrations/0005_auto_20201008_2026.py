# Generated by Django 3.1.2 on 2020-10-08 17:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mainapp', '0004_auto_20201007_1745'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cart',
            name='final_price',
            field=models.DecimalField(decimal_places=2, default=0, max_digits=9, verbose_name='Общая цена'),
        ),
    ]
