# Generated by Django 5.0.4 on 2024-04-09 18:19

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0005_socialwork'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='socialwork',
            name='title',
        ),
    ]
