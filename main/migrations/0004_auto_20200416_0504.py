# Generated by Django 3.0 on 2020-04-16 05:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0003_auto_20200416_0501'),
    ]

    operations = [
        migrations.AlterField(
            model_name='prices',
            name='extras',
            field=models.ManyToManyField(blank=True, related_name='extras', to='main.Toppings'),
        ),
    ]
