# Generated by Django 4.0.4 on 2022-05-10 04:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0003_alter_user_roles'),
    ]

    operations = [
        migrations.RenameField(
            model_name='slot',
            old_name='doctor_id',
            new_name='doctor_name',
        ),
        migrations.RemoveField(
            model_name='user',
            name='clinic_name',
        ),
        migrations.AlterField(
            model_name='user',
            name='gender',
            field=models.IntegerField(blank=True, default=None, null=True),
        ),
    ]
