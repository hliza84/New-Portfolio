# Generated by Django 4.2.2 on 2023-07-17 11:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('resume', '0007_testperson'),
    ]

    operations = [
        migrations.AlterField(
            model_name='testperson',
            name='text',
            field=models.TextField(max_length=300),
        ),
    ]
