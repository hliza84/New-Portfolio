# Generated by Django 4.2.2 on 2023-07-17 20:12

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('resume', '0010_person_user'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='person',
            name='user',
        ),
    ]
