# Generated by Django 3.1.6 on 2021-07-13 22:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0017_auto_20210712_1737'),
    ]

    operations = [
        migrations.AddField(
            model_name='donation',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='static/images'),
        ),
    ]
