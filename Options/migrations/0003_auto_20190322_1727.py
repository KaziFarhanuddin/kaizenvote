# Generated by Django 2.1.7 on 2019-03-22 11:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Options', '0002_options_model_url'),
    ]

    operations = [
        migrations.AlterField(
            model_name='options_model',
            name='image',
            field=models.CharField(max_length=70000),
        ),
    ]
