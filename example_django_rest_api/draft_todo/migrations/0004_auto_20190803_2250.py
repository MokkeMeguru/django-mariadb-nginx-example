# Generated by Django 2.2.4 on 2019-08-03 22:50

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('draft_todo', '0003_auto_20190803_2118'),
    ]

    operations = [
        migrations.AlterField(
            model_name='todoitem',
            name='importance',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.CreateModel(
            name='TodoItemAsAuth',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('todo_name', models.CharField(max_length=100)),
                ('todo_text', models.TextField(blank=True, null=True)),
                ('dead_line', models.DateTimeField()),
                ('raise_date', models.DateTimeField(auto_now_add=True)),
                ('importance', models.IntegerField(null=True)),
                ('close_date', models.DateTimeField(blank=True, null=True)),
                ('owner', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, to_field='username')),
            ],
            options={
                'ordering': ('dead_line', 'raise_date'),
            },
        ),
    ]
