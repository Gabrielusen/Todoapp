# Generated by Django 3.2.6 on 2021-12-28 14:15

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('TodoApp', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='todo',
            options={'ordering': ['-date_added']},
        ),
    ]
