# Generated by Django 4.0.4 on 2022-05-08 08:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0002_rename_appoinment_appointment'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='roles',
            field=models.CharField(choices=[('admin', 'Admin'), ('doctor', 'Doctor'), ('patiences', 'Patience')], max_length=30),
        ),
    ]
