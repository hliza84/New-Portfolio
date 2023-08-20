# Generated by Django 4.2.2 on 2023-07-27 19:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('resume', '0014_portfolioproject'),
    ]

    operations = [
        migrations.AddField(
            model_name='portfolioproject',
            name='category',
            field=models.CharField(default=1, max_length=50),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='portfolioproject',
            name='client',
            field=models.CharField(default=1, max_length=100),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='portfolioproject',
            name='url',
            field=models.URLField(default=1),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='portfolioproject',
            name='image',
            field=models.ImageField(upload_to='media'),
        ),
    ]