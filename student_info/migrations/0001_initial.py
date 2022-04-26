# Generated by Django 3.2.7 on 2022-04-24 10:38

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Student',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=250)),
                ('address', models.CharField(max_length=250)),
                ('mobile_number', models.IntegerField(blank=True, null=True)),
                ('email', models.EmailField(max_length=254)),
                ('location', models.CharField(max_length=250)),
                ('technical_skills', models.CharField(max_length=250)),
            ],
        ),
    ]