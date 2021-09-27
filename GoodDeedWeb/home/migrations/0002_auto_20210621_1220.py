# Generated by Django 3.1.6 on 2021-06-21 16:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Donation',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=30)),
                ('phonenumber', models.CharField(max_length=12)),
                ('catagorey', models.CharField(max_length=20)),
                ('image', models.CharField(max_length=1000000)),
                ('pickupordelivery', models.CharField(max_length=8)),
                ('description', models.TextField()),
            ],
        ),
        migrations.DeleteModel(
            name='test',
        ),
    ]
