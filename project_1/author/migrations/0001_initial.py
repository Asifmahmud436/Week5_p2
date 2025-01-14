# Generated by Django 5.0.6 on 2024-07-05 06:10

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Author',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=8)),
                ('last_name', models.CharField(max_length=8)),
                ('email', models.EmailField(max_length=254)),
                ('phone_no', models.CharField(max_length=12)),
                ('instrument_type', models.CharField(max_length=12)),
            ],
        ),
    ]
