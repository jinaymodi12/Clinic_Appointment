# Generated by Django 4.0.4 on 2022-05-11 06:21

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0025_alter_appointment_description_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='appointment',
            name='slot',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='myapp.slot'),
        ),
        migrations.AlterField(
            model_name='appointment',
            name='user',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='myapp.user'),
        ),
    ]
