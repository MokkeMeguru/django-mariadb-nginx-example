# Generated by Django 2.2.4 on 2019-08-03 20:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('draft_todo', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='authuser',
            name='first_name',
            field=models.CharField(blank=True, default='', max_length=1),
        ),
        migrations.AddField(
            model_name='authuser',
            name='last_name',
            field=models.CharField(blank=True, default='', max_length=1),
        ),
    ]
