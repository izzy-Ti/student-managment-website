# Generated by Django 5.2.1 on 2025-05-13 15:05

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('students', '0001_initial'),
        ('teachers', '0003_remove_mark_f_name'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='students',
            new_name='student',
        ),
    ]
