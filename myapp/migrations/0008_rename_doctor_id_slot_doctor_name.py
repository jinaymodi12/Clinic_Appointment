# Generated by Django 4.0.4 on 2022-05-10 06:05

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0007_rename_doctor_name_slot_doctor_id'),
    ]

    operations = [
        migrations.RenameField(
            model_name='slot',
            old_name='doctor_id',
            new_name='doctor_name',
        ),
    ]
