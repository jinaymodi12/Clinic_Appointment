# Generated by Django 4.0.4 on 2022-05-10 09:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0009_alter_user_gender'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='clinic_name',
            field=models.CharField(default=1, max_length=30),
            preserve_default=False,
        ),
    ]