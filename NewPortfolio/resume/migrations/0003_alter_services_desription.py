# Generated by Django 4.2.2 on 2023-07-16 21:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('resume', '0002_services_alter_education_degree_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='services',
            name='desription',
            field=models.TextField(max_length=150),
        ),
    ]
