# Generated by Django 3.1.6 on 2021-07-19 14:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0021_auto_20210714_1206'),
    ]

    operations = [
        migrations.AlterField(
            model_name='donation',
            name='id',
            field=models.AutoField(primary_key=True, serialize=False),
        ),
    ]
