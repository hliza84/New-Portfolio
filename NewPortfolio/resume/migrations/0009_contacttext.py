# Generated by Django 4.2.2 on 2023-07-17 12:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('resume', '0008_alter_testperson_text'),
    ]

    operations = [
        migrations.CreateModel(
            name='ContactText',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text', models.TextField(max_length=300)),
            ],
        ),
    ]
