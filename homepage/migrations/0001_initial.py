# Generated by Django 3.1.3 on 2021-01-01 16:50

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Haber',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, verbose_name='Haber adı')),
                ('description', models.TextField(verbose_name='Haber Metni')),
                ('image', models.CharField(max_length=50, verbose_name='Haber resmi')),
                ('created_date', models.DateTimeField(auto_now_add=True, verbose_name='Eklenme Tarihi')),
            ],
        ),
    ]
