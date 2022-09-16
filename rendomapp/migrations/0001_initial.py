# Generated by Django 4.1.1 on 2022-09-16 06:26

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Users',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('uid', models.IntegerField()),
                ('first_name', models.CharField(max_length=255)),
                ('last_name', models.CharField(max_length=200)),
                ('username', models.CharField(max_length=255)),
                ('email', models.EmailField(max_length=254)),
                ('avatar', models.TextField()),
                ('gender', models.CharField(max_length=255)),
                ('phone_number', models.CharField(max_length=12)),
                ('socil_insurance_number', models.TextField()),
                ('date_of_birth', models.CharField(max_length=255)),
            ],
        ),
    ]