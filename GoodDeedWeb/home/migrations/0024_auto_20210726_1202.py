# Generated by Django 3.1.6 on 2021-07-26 16:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0023_auto_20210726_1200'),
    ]

    operations = [
        migrations.AlterField(
            model_name='donation',
            name='id',
            field=models.BigAutoField(primary_key=True, serialize=False),
        ),
    ]
