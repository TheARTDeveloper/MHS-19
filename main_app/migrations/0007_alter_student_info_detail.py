# Generated by Django 5.0.2 on 2024-04-20 14:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0006_remove_socialwork_title'),
    ]

    operations = [
        migrations.AlterField(
            model_name='student_info',
            name='detail',
            field=models.TextField(blank=True, max_length=400),
        ),
    ]
