# Generated by Django 3.2.7 on 2022-04-24 11:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('student_info', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='student',
            name='technical_skills',
            field=models.CharField(choices=[('python', 'python'), ('java', 'java'), ('Ruby', 'Ruby'), ('Docker', 'Docker'), ('Node', 'Node'), ('JS', 'JS')], max_length=250),
        ),
    ]
