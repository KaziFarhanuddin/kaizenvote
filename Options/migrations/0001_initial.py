# Generated by Django 2.1.7 on 2019-03-22 10:19

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('Title', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Options_model',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=400)),
                ('d1', models.CharField(blank=True, max_length=400)),
                ('d2', models.CharField(blank=True, max_length=400)),
                ('d3', models.CharField(blank=True, max_length=400)),
                ('votes', models.IntegerField(default=0)),
                ('image', models.TextField()),
                ('title', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Title.Title_model')),
            ],
        ),
    ]
