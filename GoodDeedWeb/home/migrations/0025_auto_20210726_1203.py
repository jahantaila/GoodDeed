# Generated by Django 3.1.6 on 2021-07-26 16:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0024_auto_20210726_1202'),
    ]

    operations = [
        migrations.AlterField(
            model_name='donation',
            name='id',
            field=models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
    ]
