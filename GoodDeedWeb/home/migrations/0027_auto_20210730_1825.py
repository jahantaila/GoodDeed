# Generated by Django 3.1.6 on 2021-07-30 22:25

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0026_contact'),
    ]

    operations = [
        migrations.RenameField(
            model_name='contact',
            old_name='message',
            new_name='content',
        ),
    ]
