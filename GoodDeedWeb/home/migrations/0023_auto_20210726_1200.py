# Generated by Django 3.1.6 on 2021-07-26 16:00

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0022_auto_20210719_1057'),
    ]

    operations = [
        migrations.AlterField(
            model_name='donation',
            name='id',
            field=models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False),
        ),
    ]
