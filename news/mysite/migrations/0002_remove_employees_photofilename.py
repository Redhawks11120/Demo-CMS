# Generated by Django 2.1.15 on 2021-08-10 09:18

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('mysite', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='employees',
            name='PhotoFileName',
        ),
    ]