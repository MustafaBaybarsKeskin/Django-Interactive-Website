# Generated by Django 3.1.3 on 2021-01-10 12:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('homepage', '0003_auto_20210109_1812'),
    ]

    operations = [
        migrations.AlterField(
            model_name='haber',
            name='image',
            field=models.ImageField(max_length=50, upload_to='', verbose_name='Haber resmi'),
        ),
    ]
