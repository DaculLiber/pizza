# Generated by Django 3.0 on 2020-04-16 05:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0002_auto_20200416_0435'),
    ]

    operations = [
        migrations.AlterField(
            model_name='prices',
            name='size',
            field=models.CharField(choices=[('XL', 'Extra-Large'), ('L', 'Large'), ('M', 'Medium'), ('S', 'Small')], max_length=2),
        ),
    ]
