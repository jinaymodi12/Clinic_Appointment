# Generated by Django 4.0.4 on 2022-05-10 11:19

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0014_alter_appointment_user'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='appointment',
            name='patient_name',
        ),
        migrations.RemoveField(
            model_name='appointment',
            name='patients_id',
        ),
    ]
