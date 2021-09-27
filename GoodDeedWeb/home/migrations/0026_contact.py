# Generated by Django 3.1.6 on 2021-07-30 22:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0025_auto_20210726_1203'),
    ]

    operations = [
        migrations.CreateModel(
            name='Contact',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=45, null=True)),
                ('subject', models.CharField(blank=True, max_length=55, null=True)),
                ('email', models.EmailField(blank=True, max_length=30, null=True)),
                ('message', models.TextField()),
                ('date', models.CharField(blank=True, max_length=999, null=True)),
            ],
        ),
    ]
